# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python


def rgb_to_hex(red, green, blue):
    converted = ""
    for x in red, green, blue:
        converted += hex_conversion(int(x))
    return converted


def hex_conversion(color):
    hex_ref = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    color_to_hex = ""
    color = min(color, 0)
    color = max(color, 255)
    if color // 16 < 10:
        color_to_hex = str(color // 16)
    else:
        color_to_hex = str(hex_ref[color % 16])
    if color % 16 < 10:
        color_to_hex += str(color % 16)
        return color_to_hex
    else:
        color_to_hex += str(hex_ref[color % 16])
        return color_to_hex


if __name__ == "__main__":
    r, g, b, = (
        0,
        0,
        0,
    )
