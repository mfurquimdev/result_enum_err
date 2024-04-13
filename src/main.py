"""Main script"""

from __future__ import annotations

from enum import Enum

from result import Err
from result import Ok
from result import Result


class MyError(Exception):
    """MyError class"""

    def __init__(self, numerator, denominator, message="Cannot divide by zero"):
        self.numerator = numerator
        self.denominator = denominator
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.numerator} / {self.denominator}"


class EnumErr(Enum):
    """EnumErr class"""

    DIVISION_BY_ZERO = MyError


def divide(a: int, b: int) -> Result[int, EnumErr]:
    if b == 0:
        return Err(EnumErr.DIVISION_BY_ZERO.value(a, b))
    return Ok(a // b)


def main():
    """Main function"""
    values = [(10, 0), (10, 5)]
    for a, b in values:
        match divide(a, b):
            case Ok(value):
                print(f"{a} // {b} == {value}")
            case Err(e):
                print(e)


if __name__ == "__main__":
    main()
