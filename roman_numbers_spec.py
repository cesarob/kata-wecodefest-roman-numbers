from mamba import describe, context, it
from expects import expect, equal


def to_roman(number):
    if number <= 3:
        return "I" * number
    return "V" + to_roman(number - 5)


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

        # with it ("converts 7 to VII"):
