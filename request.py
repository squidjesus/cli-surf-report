import openmeteo_requests
import requests_cache
from retry_requests import retry
from surf_spot import Surf_Spot

def openmeteo_request(surf_spot: Surf_Spot) -> tuple:
    atmo_url = "https://api.open-meteo.com/v1/forecast"
    marine_url = "https://marine-api.open-meteo.com/v1/marine"

    atmo_params = {
        "latitude": surf_spot.lat,
        "longitude": surf_spot.long,
        "daily": ["sunrise", "sunset"],
        "hourly": ["wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        "current": ["temperature_2m", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        "timezone": "auto",
        "forecast_days": 1,
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
    }

    marine_params = {
        "latitude": 54.544587,
        "longitude": 10.227487,
        "hourly": ["wave_height", "wave_direction", "wave_period"],
        "current": ["wave_height", "wave_direction", "wave_period", "sea_surface_temperature"],
        "timezone": "auto",
        "forecast_days": 1,
        "length_unit": "imperial",
        "wind_speed_unit": "mph",
    }

    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    atmo_responses = openmeteo.weather_api(atmo_url, atmo_params)
    marine_responses = openmeteo.weather_api(marine_url, marine_params)

    return (atmo_responses, marine_responses)




