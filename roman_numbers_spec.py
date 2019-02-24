from mamba import describe, context, it
from expects import expect, equal

map = [
    (1000, "M"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
]


def to_roman(number):
    if number <= 3:
        return "I" * number
    if number == 4:
        return "IV"
    for key, value in map:
        if number >= key:
            return value + to_roman(number - key)


with describe("Roman numbers"):

    with context("once digit numbers"):

        with it("converts 1 to I"):
            expect(to_roman(1)).to(equal("I"))

        with it("converts 2 to II"):
            expect(to_roman(2)).to(equal("II"))

        with it("converts 3 to III"):
            expect(to_roman(3)).to(equal("III"))

        with it("converts 5 to V"):
            expect(to_roman(5)).to(equal("V"))

        with it("converts 6 to VI"):
            expect(to_roman(6)).to(equal("VI"))

        with it("converts 4 to IV"):
            expect(to_roman(4)).to(equal("IV"))

    with context("two digit numbers"):
        with it("converts 10 to X"):
            expect(to_roman(10)).to(equal("X"))

        with it("converts 11 to XI"):
            expect(to_roman(11)).to(equal("XI"))

        with it("converts 50 to L"):
            expect(to_roman(50)).to(equal("L"))

        with it("converts 51 to LI"):
            expect(to_roman(51)).to(equal("LI"))

        with it("converts 60 to LX"):
            expect(to_roman(60)).to(equal("LX"))

        with it("converts 61 to LXI"):
            expect(to_roman(61)).to(equal("LXI"))

    with context("three digit numbers"):
        with it("converts 100 to C"):
            expect(to_roman(100)).to(equal("C"))
