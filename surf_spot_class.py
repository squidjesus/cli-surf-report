

class Surf_Spot:

    def __init__(self, name: str, city: str, state:str, type: str, lat: float, long: float, opt_swells: str, opt_wind: str, notes: str):
        self.name = name
        self.city = city
        self.state = state 
        self.type = type
        self.lat = lat
        self.long = long
        self.opt_swells = opt_swells.split(",")
        self.opt_wind = opt_wind
        self.notes = notes

    def __repr__(self):
        lines = [
            f"====== {self.name.capitalize()} ======",
            f"Location: {self.city}, {self.state}",
            f"Lat x Long: {self.lat} x {self.long}",
            f"Break Type: {self.type}",
            f"Optimal Swells: {self.opt_swells}",
            f"Optimal Wind Direction: {self.opt_wind}",
            f"Notes: {self.notes}\n",
        ]
        return("\n".join(lines))
            
