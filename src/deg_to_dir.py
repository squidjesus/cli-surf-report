from surf_spot_class import Direction

# Return the closest "Direction" for a given value in degrees
def direction(degrees: int) -> Direction:
    lower = 0
    for dir in Direction:
        if degrees == dir.value:
            return dir.name
        if degrees > dir.value:
            lower = dir.value
    if degrees > (lower + 11.25):
        return Direction(lower + 22.5).name
    else:
        return Direction(lower).name