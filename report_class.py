from surf_spot_class import Surf_Spot
from datetime import datetime
from quality_calcs import wind_dir_rating, swell_dir_rating, swell_size_rating, swell_per_rating, direction

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
            daily.Variables(0).ValuesInt64(0),
            daily.Variables(1).ValuesInt64(0)
        ]

        #Atmo Hourly: [wind speed, wind direction, wind gusts]
        #hrly_atmo = self.atmo_response.Hourly()
        #hrly_atmo_vars = [
        #    hrly_atmo.Variables(0).ValuesAsNumpy(),
        #    hrly_atmo.Variables(1).ValuesAsNumpy(), 
        #    hrly_atmo.Variables(2).ValuesAsNumpy()
        #]

        #Marine Hourly: [wave height, wave direction, wave period]
        #hrly_marine = self.marine_response.Hourly()
        #hrly_marine_vars = [
        #    hrly_marine.Variables(0).ValuesAsNumpy(),
        #   hrly_marine.Variables(1).ValuesAsNumpy(),
        #   hrly_marine.Variables(2).ValuesAsNumpy()
        #

        #Time data
        #self.atmo_hourly_time = datetime.fromtimestamp(hrly_atmo.Time())
        #self.atmo_hourly_time_end = datetime.fromtimestamp(hrly_atmo.TimeEnd())
        #self.atmo_hourly_interval = hrly_atmo.Interval()

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
        dt_sr = datetime.fromtimestamp(daily_atmo[0])
        self.sunrise = dt_sr.strftime('%I:%M %p')
        dt_ss = datetime.fromtimestamp(daily_atmo[1])
        self.sunset = dt_ss.strftime('%I:%M %p')

        #self.hr_wind_speed = hrly_atmo_vars[0]
        #self.hr_wind_direction = hrly_atmo_vars[1]
        #self.hr_wind_gust = hrly_atmo_vars[2]

        #self.hourly_wave_height = hrly_marine_vars[0]
        #self.hourly_wave_dir = hrly_marine_vars[1]
        #self.hourly_wave_per = hrly_marine_vars[2]

        self.current_atmo_temp = round(current_atmo_vars[0])
        self.current_wind_speed = round(current_atmo_vars[1])
        self.current_wind_dir = round(current_atmo_vars[2])
        self.current_wind_gust = round(current_atmo_vars[3])

        self.current_wave_height = round(current_marine_vars[0], 1)
        self.current_wave_dir = round(current_marine_vars[1])
        self.current_wave_per = round(current_marine_vars[2])
        self.current_water_temp = round(current_marine_vars[3])


        #ratings:
        self.wind_dir_rating = wind_dir_rating(self)[0].value
        self.wind_condition = wind_dir_rating(self)[1].value
        self.swell_dir_rating = swell_dir_rating(self).value
        self.swell_size_rating = swell_size_rating(self).value
        self.swell_per_rating = swell_per_rating(self).value

    def __repr__(self):
        all_props = []
        for key, value in vars(self).items():
            all_props.append(f"{key}: {value}")
        props = "\n".join(all_props)
        return props
    

    def current_report(self):
        data = {
            'Name'          : self.surf_spot.name,
            'Location'      : self.surf_spot.location,
            'Facing'        : f"{self.surf_spot.facing.name}",
            'Swell'         : f"[{self.swell_size_rating}]{self.current_wave_height}ft[/{self.swell_size_rating}]",
            'Period'        : f"[{self.swell_per_rating}]{self.current_wave_per}s[/{self.swell_per_rating}]",
            'Dir'           : f"[{self.swell_dir_rating}]{direction(self.current_wave_dir)}: {self.current_wave_dir}{chr(176)}[/{self.swell_dir_rating}]",
            'Wind'          : f"[{self.wind_dir_rating}]{self.current_wind_speed}mph {self.wind_condition}[/{self.wind_dir_rating}]",
            'Wind-Dir'      : f"[{self.wind_dir_rating}]{direction(self.current_wind_dir)}: {self.current_wind_dir}{chr(176)}[/{self.wind_dir_rating}]",
            'Air'           : f"{self.current_atmo_temp}{chr(176)} F",
            'Water'         : f"{self.current_water_temp}{chr(176)} F",
            'Sunrise'       : self.sunrise,
            'Sunset'        : self.sunset
        }
        return data
    

    def multiline_report(self):
        pass