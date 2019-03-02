map = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I"
}

substractors = [100, 10, 1]


def to_roman(number):
    if number == 0:
        return ''
    for key, value in map.items():
        if number >= key:
            return value + to_roman(number - key)
        for sub in substractors:
            if number + sub == key:
                return map[sub] + to_roman(number + sub)
