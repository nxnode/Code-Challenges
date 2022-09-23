# https://www.codewars.com/kata/5266876b8f4bf2da9b000362


def who_likes(names):
    if len(names) == 0:
        names = "no one likes this"
    elif len(names) == 1:
        names = names[0] + " likes this"
    elif len(names) == 2:
        names = names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        names = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) > 3:
        names = (
            names[0]
            + ", "
            + names[1]
            + " and "
            + str(len(names) - 2)
            + " others like this"
        )
    return names
