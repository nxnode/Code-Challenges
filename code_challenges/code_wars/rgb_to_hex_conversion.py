# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python


def rgb_to_hex(*args):
    return "{}{}{}".format(
        *(f"{'' if x > 16 else 0}{x:X}" for x in (min(max(x, 0), 255) for x in args))
    )


if __name__ == "__main__":
    print(rgb_to_hex(255, 255, 255))
