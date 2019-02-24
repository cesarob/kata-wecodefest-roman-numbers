from mamba import describe, context, it
from expects import expect, equal


def to_roman(number):
    return "I"


with describe("Roman numbers"):

    with context("once digit numbers"):

        with it("converts 1 to I"):
            expect(to_roman(1)).to(equal("I"))

        # with it ("converts 2 to II"):
        # with it ("converts 3 to III"):
        # with it ("converts 5 to V"):
        # with it ("converts 6 to VI"):
        # with it ("converts 7 to VII"):
