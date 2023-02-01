# https://www.codewars.com/kata/550f22f4d758534c1100025a/python


def directions_reduction(directions):
    reduced_directions = []
    direction_ref = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    for direction in directions:
        try:
            prev_direction = reduced_directions[-1]
        except IndexError:
            prev_direction = None
        if direction_ref[direction] != prev_direction:
            reduced_directions.append(direction)
        else:
            reduced_directions.pop()
    return reduced_directions
