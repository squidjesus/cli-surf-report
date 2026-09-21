from enum import Enum
from src.deg_to_dir import direction

class Rating(Enum):
    BLANK = 'white'
    IDEAL = 'blue'
    GOOD = 'green'
    MID = 'yellow'
    POOR = 'red'

class Wind(Enum):
    OFFSHORE = 'Offshore'
    CROSSSHORE = 'Cross-shore'
    ONSHORE = 'Onshore'

# Return a dict with the current report data for a pd dataframe

def current_report_dict(report):
    data = {
        'Surf Spot' : [report.surf_spot.name],
        'Location'  : [report.surf_spot.location],
        'Facing' : [report.surf_spot.facing],
        'Sw Height' : [report.current_wave_height],
        'Sw Period' : [report.current_wave_per],
        'Sw Dir' : [direction(report.current_wave_dir)],
        'Wind' : [report.current_wind_speed],
        'Wind Dir' : [direction(report.current_wind_dir)],
        'Air Temp' : [report.current_atmo_temp],
        'Water Temp' : [report.current_water_temp],
        'Sunrise' : [report.sunrise],
        'Sunset' : [report.sunset]
    }
    return data


# Return a dict with a timestamp added to each hourly data entry
def hrly_data_times(data: list) -> dict:
    data_times = {}
    i = 1
    for item in data:
        data_times[f'{i}:00'] = item
        i += 1
    return data_times


# Return the rating for current wind conditions at the spot
def wind_dir_rating(report) -> tuple:
    facing = report.surf_spot.facing.value
    wind_dir = report.current_wind_dir
    speed = report.current_wind_speed

    offset = abs((facing - wind_dir + 360) % 360 - 180)

    if offset <= 15:
        rating = Rating.BLANK if speed <= 3 else Rating.IDEAL if speed <= 10 else Rating.GOOD if speed <= 20 else Rating.MID
        return rating, Wind.OFFSHORE
    if offset <= 45:
        rating = Rating.BLANK if speed <= 3 else Rating.GOOD if speed <= 10 else Rating.MID if speed <= 20 else Rating.POOR
        return rating, Wind.OFFSHORE
    if offset <= 135:
        rating = Rating.BLANK if speed <= 3 else Rating.MID if speed <= 10 else Rating.POOR
        return rating, Wind.CROSSSHORE
    else:
        rating = Rating.BLANK if speed <= 2 else Rating.MID if speed <= 5 else Rating.POOR
        return rating, Wind.ONSHORE


# Return the rating for current swell conditions at the spot. To Do: Add complexity for swell height/period
def swell_dir_rating(report) -> Rating:
    facing = report.surf_spot.facing.value
    swell_dir = report.current_wave_dir

    offset = abs((facing - swell_dir + 540) % 360 - 180)
    
    if offset <= 10:
        return Rating.IDEAL
    if offset <= 20:
        return Rating.GOOD
    if offset <= 90:
        return Rating.MID
    return Rating.POOR


def swell_size_rating(report) -> Rating:
    size = report.current_wave_height
    if size < 1.5:
        return Rating.POOR
    if size < 3:
        return Rating.MID
    if size < 5:
        return Rating.GOOD
    return Rating.IDEAL

def swell_per_rating(report) -> Rating:
    p = report.current_wave_per
    if p < 3:
        return Rating.POOR
    if p < 8:
        return Rating.MID
    if p < 15:
        return Rating.GOOD
    return Rating.IDEAL





