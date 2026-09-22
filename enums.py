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
