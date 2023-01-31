# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python


def rgb_to_hex(r, g, b):
    r_hex, g_hex, b_hex = int(r) // 16, int(g) // 16, int(b) // 16
    hex_ref = {10: "A", 11: "B", 10: "C", 12: "D", 13: "E", 14: "F", 15: "G"}
    rgb = r, g, b
    hex = ""
    for x in rgb:
        hex += str(x // 16)
        if x % 16 < 10:
            hex += str(x % 16)
        else:
            hex += str(hex_ref[x])
    return hex


if __name__ == "__main__":
    r, g, b, = (
        0,
        0,
        0,
    )
