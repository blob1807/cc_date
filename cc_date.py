import re
import dataclasses
from string import ascii_uppercase
from typing import Optional, Any, Generator

__doc__ = """For use with Ivycomb's Cosmic Critters date format."""


# ========== CC Date Format Class ============
class cc_format:
    """
    Docstring to be implemented\n
    -Blob
     """
    valid_string_formats = '!1234 aAa 123 | !1234aAa123 \n1234 aAa 123 | 1234aAa123\n' \
                           '1234 A 123 | A 123 | 1234 A \n1234A123 | A123 | 1234A \n' \
                           '234123 | aAa'
    valid_digits_format = '[0-inf, 0-25, 0-25, 0-25, 0-999] \n(0-inf, 0-25, 0-25, 0-25, 0-999)'
    cc_format = '!YYYY MMM DDD', '!1234 ABC 567'
    regex = re.compile(r'!?\d+ ?[a-z]{3} ?\d{3}(?=\D|\Z)', re.IGNORECASE)
    regex_greedy = re.compile(r'(\d*) *([a-z]+) *(\d*(?=\D|\Z))', re.IGNORECASE)


class normalize:
    """
    Docstring to be implemented\n
    -Blob
    """

    @staticmethod
    def evaluate(dates: list[str | int | list | tuple]) -> list[str | int | list | tuple]:
        """\t
        :param dates: list of dates to be evaluated
        :return: evaluated list of dates
        """
        for pos, date in enumerate(dates):
            assert date, f"Date, {repr(date)}, must not be empty"
            try:
                # Semi safe eval.
                date = eval(date, {'__builtins__': None})

            except SyntaxError as e:
                if not cc_format.regex_greedy.findall(date):
                    raise e

            except TypeError:
                raise Exception(f'{date} is not a date')

            else:
                if type(date) not in {int, list, tuple}:
                    raise Exception(f'{date} is invalid date format')
                dates[pos] = date

        return dates

    @staticmethod
    def string(date: str) -> str:
        assert date.upper().isupper(), f'Date: {date} must have at least 1 letter.'
        work = list(cc_format.regex_greedy.findall(date)[0])
        while len(work[1]) < 3:
            work[1] += 'A'
        return f'!{work[0].zfill(1)} {work[1].upper()} {work[2].zfill(3)}'

    @staticmethod
    def digits(date: list[int] | tuple[int, ...]) -> list[int, int, int, int, int]:
        base26 = '0123456789abcdefghijklmnop'
        date = list(date)

        if len(date) < 5:
            # Make date be at least 5 long
            date = date[::-1]
            date.extend([0] * (5 - len(date)))
            date = date[::-1]

        if len(date) > 5:
            # Handle for when 4 or more Letters were provided; !1234 BAAB 123 -> [1234, 1, 0, 0, 1, 123]
            date[0] += int(''.join(base26[d] for d in date[1:-4]) + '0', 26)
            del date[1:-4]  # Remove any extra letters.

        return date


# ============== CC Date Class ===============
@dataclasses.dataclass
class cc_date:
    """
    Docstring to be implemented\n
    -Blob
     """
    date: list[int] | tuple[int, ...] | str | int  # Always converts to int
    radixes: Optional[list[int]] = dataclasses.field(default_factory=list)
    weights: Optional[list[int]] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        assert type(self.date) in {list, tuple, str, int}, f'Date, {repr(self.date)}, must be list, tuple, str or int'
        assert type(self.weights) is list, f'Weights, {repr(self.weights)}, must be a list'
        assert type(self.radixes) is list, f'Radixes, {repr(self.radixes)}, must be a list'
        # Add eval check here?

        # Normalize & Convert to Digits Date
        if type(self.date) in {list, tuple}:
            self.date = normalize.digits(self.date)

        elif type(self.date) is str:
            if not self.date.upper().isupper():
                self.date = f'!000 AAA {self.date.zfill(3)}'

            self.date = normalize.string(self.date)
            self.date = convert.string_to_digits(self.date)

        else:
            self.date = convert.decimal_to_digits(self.date)

        # Use Digits Date to calculate Radix & Weights
        if not self.radixes:
            self.radixes = calc.radixes(self.date)
        if not self.weights:
            self.weights = calc.weights(self.radixes)

        # Make date Decimal Date
        self.date = convert.digits_to_decimal(self.date, self.weights)

    @property
    def decimal(self) -> int:
        """
        :return: CC Date in Decimal format
        """
        assert type(self.date) is int, \
            "cc_date.date shouldn't be modified after initialization."
        return self.date

    @property
    def digits(self) -> tuple[int, ...]:
        """
        :return: CC Date in Digits format
        """
        assert type(self.date) is int, \
            "cc_date.date shouldn't be modified after initialization."
        return tuple(convert.decimal_to_digits(self.date))

    @property
    def string(self) -> str:
        """
        :return: CC Date in String format
        """
        assert type(self.date) is int, \
            "cc_date.date shouldn't be modified after initialization."
        return convert.decimal_to_string(self.date)


# ============ Calculation Class ============
class calc:
    """
    Docstring to be implemented\n
    -Blob
    """

    @staticmethod
    def radixes(date: list[int]) -> list[int, int, int, int, int]:
        """\t
        :param date: CC Date in Digits format
        :return: Radixes of given date
        """
        return [10 ** len(repr(date[0])), 26, 26, 26, 1000]

    @staticmethod
    def weights(radixes: list[int]) -> list[int, int, int, int, int]:
        """\t
        :param radixes: Radixes of a date
        :return: Weights of given Radixes
        """
        return [radixes[1] * 676000, 676000, 26000, 1000, 1]


# ============= Conversion Class =============
class convert:
    """
    Docstring to be implemented\n
    -Blob
    """

    @staticmethod
    def digits_to_decimal(date: list[int], weights: Optional[list[int]] = ...) -> int:
        # Mixed to Base10
        # NEEDS to be normalized with normalize.digits() before passing to this func
        if weights is Ellipsis or not weights:
            weights = calc.weights(calc.radixes(date))
        # Multiple each date by its weight & sum them up
        return sum(map(lambda weight, n: weight * n, weights, date))

    @staticmethod
    def decimal_to_digits(date: int) -> list[int, int, int, int, int]:
        # Base10 to Mixed
        work = []
        for r in (26, 26, 26, 1000)[::-1]:
            # Loop through radixes. Excluding 5th radix.
            work.append(date % r)
            date //= r
        # Append what's left. Same as if 5th radix is used.
        work.append(date)
        return work[::-1]

    @staticmethod
    def digits_to_string(date: list[int]) -> str:
        # NEEDS to be normalized with normalize.digits() before passing to this func
        return f"!{date[0]} {ascii_uppercase[date[1]]}{ascii_uppercase[date[2]]}{ascii_uppercase[date[3]]} {date[4]}"

    @staticmethod
    def string_to_digits(date: str) -> list[int, int, int, int, int]:
        # NEEDS to be normalized with normalize.string() before passing to this func
        date = date.lstrip('!').split(' ')
        work = [int(date[0])]

        for letter in date[1]:
            work.append(ascii_uppercase.index(letter.upper()))

        work.append(int(date[2]))
        return normalize.digits(work)

    @staticmethod
    def decimal_to_string(date: int) -> str:
        return convert.digits_to_string(convert.decimal_to_digits(date))

    @staticmethod
    def string_to_decimal(date: str, weights: Optional[list[int]] = ...) -> int:
        # NEEDS to be normalized with normalize.string() before passing to this func
        return convert.digits_to_decimal(convert.string_to_digits(date), weights)


# ================ Math Class ================
class cc_math:
    """
    Docstring to be implemented\n
    -Blob
     """

    @staticmethod
    def add(dates: list[cc_date]) -> cc_date:
        """
        Adds CC Dates
        :param dates: list of cc_date
        :return: cc_date
        """
        assert len(dates) > 1
        ans = 0
        for date_ in dates:
            ans += date_.decimal
        return cc_date(ans)

    @staticmethod
    def sub(dates: list[cc_date]) -> cc_date:
        """
        Subtracts CC Dates
        :param dates: list of cc_date
        :return: cc_date
        """
        assert len(dates) > 1
        ans = dates[0].decimal
        for date_ in dates[1:]:
            ans -= date_.decimal
        return cc_date(ans)

    @staticmethod
    def mul(dates: list[cc_date]) -> cc_date:
        """
        Multiples CC Dates
        :param dates: list of cc_date
        :return: cc_date
        """
        assert len(dates) > 1
        ans = 1
        for date_ in dates:
            ans *= date_.decimal
        return cc_date(ans)

    @staticmethod
    def div(dates: list[cc_date]) -> cc_date:
        """
        Floor Divides CC Dates
        :param dates: list of cc_date
        :return: cc_date
        """
        assert len(dates) > 1
        ans = dates[0].decimal
        for date_ in dates[1:]:
            ans //= date_.decimal
        return cc_date(ans)


def cli():
    """Used only as Command Line Tool"""
    if __name__ != '__main__':
        raise Exception("For CLI use only.")

    import argparse
    parser = argparse.ArgumentParser(description="For use with Ivycomb's Cosmic Critters date format.")
    parser.add_argument('--cleanout', help='Makes output clean for easier copying.', action='store_true')

    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument('-a', '--add', help='Add 2 or more CC Dates', action='store_true')
    operation.add_argument('-s', '--sub', help='Sub 2 or more CC Dates', action='store_true')
    operation.add_argument('-m', '--multiple', help='Multiple 2 or more CC Dates', action='store_true')
    operation.add_argument('-d', '--divide', help='Floor Divide 2 or more CC Dates', action='store_true')

    operation.add_argument('-f', '--valid-formats', help='Prints all valid input formats', action='store_true')

    operation.add_argument('-c', '--convert', choices=['string', 'digits', 'decimal'],
                           help='Convert from String, Digits & Decimal Dates to String, Digits or Decimal Dates')
    operation.add_argument('-C', '--calculate', choices=['radix', 'weights'],
                           help='Calculates the Radixes or Weights of given Date\\s')
    operation.add_argument('-n', '--normalize', choices=['string', 'digits'],
                           help='Normalize strings & arrays to expected formats. Script does this automatically.')

    parser.add_argument('dates', help='CC Dates', nargs='+')
    # parser.print_help()

    # inp = ['-c', 'string', "!1234 ABC 123", "!1234ABC123", '(1234, 0, 1, 2, 123)', '21688812123']
    # inp = ['-n', 'string', '!14ABC13', '1234 A123']
    # args = parser.parse_args(inp)
    args = parser.parse_args()

    args.dates = normalize.evaluate(args.dates)

    if args.add:
        values = cc_math.add([cc_date(date) for date in args.dates]).string
    elif args.sub:
        values = cc_math.sub([cc_date(date) for date in args.dates]).string
    elif args.multiple:
        values = cc_math.mul([cc_date(date) for date in args.dates]).string
    elif args.divide:
        values = cc_math.div([cc_date(date) for date in args.dates]).string

    elif args.valid_formats:
        values = f'Valid Input Formats:\n' \
                 f'String & Decimal:\n{cc_format.valid_string_formats}\n\n' \
                 f'Digits:\n{cc_format.valid_digits_format}'

    elif args.convert:
        if args.convert == 'string':
            print("Dates converted to String format:")
            values = (cc_date(date).string for date in args.dates)

        elif args.convert == 'digits':
            print("Dates converted to Digits format:")
            values = (cc_date(date).digits for date in args.dates)

        else:
            print("Dates converted to Decimal format:")
            values = (cc_date(date).decimal for date in args.dates)

    elif args.calculate:
        if args.calculate == 'radix':
            print("Place value Radixes:")
            values = (cc_date(date).radixes for date in args.dates)

        else:
            print("Place value Weights:")
            values = (cc_date(date).weights for date in args.dates)

    elif args.normalize:
        if args.normalize == 'string':
            print("String Dates Normalized:")
            values = (normalize.string(date) for date in args.dates)

        else:
            print("Digit Dates Normalized:")
            values = (normalize.digits(date) for date in args.dates)

    else:
        raise Exception("Do look at me. Argparse must of decide to go poof.")

    if isinstance(values, Generator):
        if args.cleanout:
            print(*values)
        else:
            for date, value in zip(args.dates, values):
                print(f'{date} -> {value}')
    else:
        print(values)

    return 0


if __name__ == '__main__':
    import sys

    cli()
    sys.exit(0)
