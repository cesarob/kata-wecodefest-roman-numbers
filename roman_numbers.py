map = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def to_roman(number):
    if number == 0:
        return ''
    for key, value in map.items():
        if number >= key:
            return value + to_roman(number - key)
