from mamba import describe, context, it
from expects import expect, equal

from roman_numbers import to_roman

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

        with it("converts 40 to XL"):
            expect(to_roman(40)).to(equal("XL"))

        with it("converts 90 to XC"):
            expect(to_roman(90)).to(equal("XC"))

    with context("three digit numbers"):
        with it("converts 100 to C"):
            expect(to_roman(100)).to(equal("C"))

        with it("converts 500 to C"):
            expect(to_roman(500)).to(equal("D"))

        with it("converts 400 to CD"):
            expect(to_roman(400)).to(equal("CD"))

        with it("converts 400 to CD"):
            expect(to_roman(400)).to(equal("CD"))

    with context("4 digit numbers"):
        with it("converts 1000 to M"):
            expect(to_roman(1000)).to(equal("M"))

    with context("more than one substraction"):
        with _it("converts 99 to XCIX"):
            expect(to_roman(99)).to(equal("XCIX"))
