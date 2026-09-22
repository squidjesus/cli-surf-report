from enums import Rating, Wind, Direction


# Return the rating for current wind conditions at the spot
def wind_dir_rating(report) -> tuple:
    facing = report.surf_spot.facing.value
    wind_dir = report.current_wind_dir
    speed = report.current_wind_speed

    offset = abs((facing - wind_dir + 360) % 360 - 180)

    if offset <= 15:
        rating = Rating.BLANK if speed <= 3 else Rating.IDEAL if speed <= 15 else Rating.GOOD if speed <= 20 else Rating.MID
        return rating, Wind.OFFSHORE
    if offset <= 45:
        rating = Rating.BLANK if speed <= 3 else Rating.GOOD if speed <= 15 else Rating.MID if speed <= 20 else Rating.POOR
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
    if offset <= 30:
        return Rating.GOOD
    if offset <= 100:
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