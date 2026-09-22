import openmeteo_requests
from surf_spot_class import Surf_Spot

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
        "latitude": surf_spot.lat,
        "longitude": surf_spot.long,
        "hourly": ["wave_height", "wave_direction", "wave_period"],
        "current": ["swell_wave_height", "swell_wave_direction", "swell_wave_period", "sea_surface_temperature"],
        "timezone": "auto",
        "forecast_days": 1,
        "length_unit": "imperial",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
    }

    openmeteo = openmeteo_requests.Client()

    atmo_responses = openmeteo.weather_api(atmo_url, atmo_params)
    marine_responses = openmeteo.weather_api(marine_url, marine_params)

    return (atmo_responses[0], marine_responses[0])




