from enums import Direction

class Surf_Spot:

    def __init__(self, id: int, name: str, location: str, type: str, lat: float, long: float, facing: Direction, notes: str):
        self.id = id
        self.name = name
        self.location = location
        self.type = type
        self.lat = lat
        self.long = long
        self.facing = Direction[facing]
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
            
