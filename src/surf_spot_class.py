from enum import Enum

class Direction(Enum):
    N = 0.0
    NNE = 22.5
    NE = 45.0
    ENE = 67.5
    E = 90.0
    ESE = 112.5
    SE = 135
    SSE = 157.5
    S = 180.0
    SSW = 202.5
    SW = 225
    WSW = 247.5
    W = 270.0
    WNW = 292.5
    NW = 315.0
    NNW = 337.5

class Surf_Spot:

    def __init__(self, id: int, name: str, location: str, type: str, lat: float, long: float, facing: Direction, notes: str):
        self.id = id
        self.name = name
        self.location = location
        self.type = type
        self.lat = lat
        self.long = long
        self.facing = facing
        self.notes = notes

    def __repr__(self):
        lines = [
            f"====== {self.name.capitalize()} ======",
            f"Location: {self.location}",
            f"Lat x Long: {self.lat} x {self.long}",
            f"Break Type: {self.type}",
            f"Facing Direction: {self.facing}"
            f"Notes: {self.notes}\n",
        ]
        return("\n".join(lines))
            
