from surf_spot_class import Surf_Spot, Direction
from report_class import Report
from surf_spot_class import Surf_Spot
from deg_to_dir import direction

# Return a dict with the current report data for a pd dataframe

def current_report_dict(report: Report):
    data = {
        'Surf Spot' : [report.surf_spot.name],
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


# Return an int representing the offset from the "optimal" value for the surf spot
def opt_offset(data: int, value: Direction) -> int:
    opt_value = 360 - abs(value - 180)
    return int(abs(opt_value - data))


# Return "color" for wind data according to the magnitude and offset from optimal conditions
def wind_color_code(data: int, offset: int) -> str:
    pass


# Return the "color" for swell data according to the magnitude and offset from optimal conditions
def swell_color_code(data: int, offset: int) -> str:
    pass


# Return a readable version of the passed data depending on data type
def format(data):
    pass


