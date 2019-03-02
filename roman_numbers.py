MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]


def to_roman(number, map=MAP):
    if len(map) == 0:
        return ''
    decimal, roman = map[0]
    if number > decimal:
        return roman + to_roman(number - decimal, map)
    elif number == decimal:
        return roman
    else:
        return to_roman(number, map[1:])
