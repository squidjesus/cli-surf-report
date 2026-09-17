import pandas as pd
from surf_spot_class import Surf_Spot
from datetime import datetime
from deg_to_dir import direction

class Report:

    def __init__(self, responses: tuple, surf_spot: Surf_Spot):
        self.atmo_response = responses[0]
        self.marine_response = responses[1]
        self.surf_spot = surf_spot

        self.latitude = surf_spot.lat
        self.longitude = surf_spot.long

        #Atmo Daily: [sunrise, sunset]
        daily = self.atmo_response.Daily()
        daily_atmo = [
            daily.Variables(0).ValuesInt64AsNumpy(),
            daily.Variables(1).ValuesInt64AsNumpy()
        ]

        #Atmo Hourly: [wind speed, wind direction, wind gusts]
        hrly_atmo = self.atmo_response.Hourly()
        hrly_atmo_vars = [
            hrly_atmo.Variables(0).ValuesAsNumpy(),
            hrly_atmo.Variables(1).ValuesAsNumpy(), 
            hrly_atmo.Variables(2).ValuesAsNumpy()
        ]

        #Marine Hourly: [wave height, wave direction, wave period]
        hrly_marine = self.marine_response.Hourly()
        hrly_marine_vars = [
            hrly_marine.Variables(0).ValuesAsNumpy(),
            hrly_marine.Variables(1).ValuesAsNumpy(),
            hrly_marine.Variables(2).ValuesAsNumpy()
        ]

        #Time data
        self.atmo_hourly_time = datetime.fromtimestamp(hrly_atmo.Time())
        self.atmo_hourly_time_end = datetime.fromtimestamp(hrly_atmo.TimeEnd())
        self.atmo_hourly_interval = hrly_atmo.Interval()

        #Atmo Current: [temp, wind speed, wind direction, wind gusts]
        current_atmo = self.atmo_response.Current()
        current_atmo_vars = [
            current_atmo.Variables(0).Value(),
            current_atmo.Variables(1).Value(),
            current_atmo.Variables(2).Value(),
            current_atmo.Variables(3).Value()
        ]

        #Marine Current: [wave height, wave direction, wave period, water temp]
        current_marine = self.marine_response.Current()
        current_marine_vars = [
            current_marine.Variables(0).Value(),
            current_marine.Variables(1).Value(),
            current_marine.Variables(2).Value(),
            current_marine.Variables(3).Value()
        ] 

        #Weather Data Properties
        dt_sr = datetime.fromtimestamp(daily_atmo[0][0])
        self.sunrise = dt_sr.strftime('%I:%M %p')
        dt_ss = datetime.fromtimestamp(daily_atmo[1][0])
        self.sunset = dt_ss.strftime('%I:%M %p')

        self.hr_wind_speed = hrly_atmo_vars[0]
        self.hr_wind_direction = hrly_atmo_vars[1]
        self.hr_wind_gust = hrly_atmo_vars[2]

        self.hourly_wave_height = hrly_marine_vars[0]
        self.hourly_wave_dir = hrly_marine_vars[1]
        self.hourly_wave_per = hrly_marine_vars[2]

        self.current_atmo_temp = round(current_atmo_vars[0])
        self.current_wind_speed = round(current_atmo_vars[1])
        self.current_wind_dir = round(current_atmo_vars[2])
        self.current_wind_gust = round(current_atmo_vars[3])

        self.current_wave_height = round(current_marine_vars[0], 1)
        self.current_wave_dir = round(current_marine_vars[1])
        self.current_wave_per = round(current_marine_vars[2])
        self.current_water_temp = round(current_marine_vars[3])


    def __repr__(self):
        all_props = []
        for key, value in vars(self).items():
            all_props.append(f"{key}: {value}")
        props = "\n".join(all_props)
        return props
    

    def current_report(self):
        data = {
            'Surf-Spot' : self.surf_spot.name,
            'Facing' : self.surf_spot.facing,
            'Sw-Height' : f"{self.current_wave_height}ft",
            'Sw-Period' : f"{self.current_wave_per}s",
            'Sw-Dir' : f"{direction(self.current_wave_dir)}: {self.current_wave_dir}{chr(176)}",
            'Wind' : self.current_wind_speed,
            'Wind-Dir' : direction(self.current_wind_dir),
            'Air-Temp' : f"{self.current_atmo_temp}{chr(176)} F",
            'Water-Temp' : f"{self.current_water_temp}{chr(176)} F",
            'Sunrise' : self.sunrise,
            'Sunset' : self.sunset
        }
        return data
    

    def multiline_report(self):
        pass