import re
import dataclasses
from string import ascii_uppercase

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
    valid_digits_format = '[0-inf, 0-26, 0-26, 0-26, 0-999]'
    cc_format = '!1234 AAA 123'
    regex = re.compile(r'!?\d+ ?[a-z]{3} ?\d{3}(?=\D|\Z)', re.IGNORECASE)
    regex_greedy = re.compile(r'(\d*) *([a-z]+) *(\d*(?=\D|\Z))', re.IGNORECASE)

    class normalize:
        """
        Docstring to be implemented\n
        -Blob
         """
        # Add eval check here?
        # def evaluate(dates: list | tuple) -> list | tuple:
        @staticmethod
        def string(date: any) -> str:
            work = list(cc_format.regex_greedy.findall(date)[0])
            while len(work[1]) < 3:
                work[1] += 'A'
            return f'!{work[0].zfill(1)} {work[1].upper()} {work[2].zfill(3)}'

        @staticmethod
        def digits(date: list | tuple) -> tuple:
            base26 = '0123456789abcdefghijklmnop'
            if len(date) >= 6:
                # Handle for when 4 or more Letters were provided; !1234 BAAB 123 -> [1234, 1, 0, 0, 1, 123]
                date = list(date)
                date[0] += int(''.join(base26[d] for d in date[1:-4]) + '0', 26)
                del date[1:-4]
            return tuple(date)


# ============== CC Date Class ===============
@dataclasses.dataclass
class cc_date:
    """
    Docstring to be implemented\n
    -Blob
     """
    date: list | tuple | str | int  # Always converts to int
    radixes: list | tuple = dataclasses.field(default_factory=list)
    weights: list | tuple = dataclasses.field(default_factory=list)

    def __post_init__(self):
        assert self.date, f"Date, {repr(self.date)}, must not be empty"
        assert type(self.date) in (list, tuple, str, int), f'Date, {repr(self.date)}, must be list, tuple, str or int'
        assert type(self.weights) in (list, tuple), f'Weights, {repr(self.weights)}, must be list or tuple'
        assert type(self.radixes) in (list, tuple), f'Radixes, {repr(self.radixes)}, must be list or tuple'
        # Add eval check here?

        # Normalize & Convert to Digits Date
        if type(self.date) in (list, tuple):
            self.date = cc_format.normalize.digits(self.date)
        elif type(self.date) is str:
            self.date = cc_format.normalize.string(self.date)
            self.date = convert.string_to_digits(self.date)
        elif type(self.date) is int:
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
            "cc_date.date shouldn't be modified after initialization. Must stay an int."
        return self.date

    @property
    def digits(self) -> tuple:
        """
        :return: CC Date in Digits format
        """
        assert type(self.date) is int, \
            "cc_date.date shouldn't be modified after initialization. Must stay an int."
        return convert.decimal_to_digits(self.date)

    @property
    def string(self) -> str:
        """
        :return: CC Date in String format
        """
        assert type(self.date) is int, \
            "cc_date.date shouldn't be modified after initialization. Must stay an int."
        return convert.decimal_to_string(self.date)


# ============ Calculation Class ============
class calc:
    """
    Docstring to be implemented\n
    -Blob
    """
    @staticmethod
    def radixes(date: list | tuple) -> tuple:
        """
        :param date: CC Date in Digits format
        :return: Radixes of given date
        """
        return 10 ** len(repr(date[0])), 26, 26, 26, 1000

    @staticmethod
    def weights(radixes: list | tuple) -> tuple:
        """
        :param radixes: Radixes of a date
        :return: Weights of given Radixes
        """
        return radixes[1]*676000, 676000, 26000, 1000, 1


# ============= Conversion Class =============
class convert:
    """
    Docstring to be implemented\n
    -Blob
     """
    @staticmethod
    def digits_to_decimal(date: list | tuple,
                          weights: list | tuple = ...) -> int:
        # Mixed to Base10
        # NEEDS to be normalized with cc_format.normalize.digits() before passing to this func
        if weights is Ellipsis or not weights:
            weights = calc.weights(calc.radixes(date))
        # Multiple each date by its weight & sum them up
        return sum(map(lambda weight, n: weight * n, weights, date))

    @staticmethod
    def decimal_to_digits(date: int) -> tuple:
        # Base10 to Mixed
        work = []
        for r in (26, 26, 26, 1000)[::-1]:
            # Loop through radixes. Excluding 5th radix.
            work.append(date % r)
            date //= r
        # Append what's left. Same as if 5th radix is used.
        work.append(date)
        return tuple(work[::-1])

    @staticmethod
    def digits_to_string(date: list | tuple) -> str:
        # NEEDS to be normalized with cc_format.normalize.digits() before passing to this func
        return f"!{date[0]} {ascii_uppercase[date[1]]}{ascii_uppercase[date[2]]}{ascii_uppercase[date[3]]} {date[4]}"

    @staticmethod
    def string_to_digits(date: str) -> tuple:
        # NEEDS to be normalized with cc_format.normalize.string() before passing to this func
        date = date.lstrip('!').split(' ')
        work = [int(date[0])]

        for letter in date[1]:
            work.append(ascii_uppercase.index(letter.upper()))

        work.append(int(date[2]))
        return cc_format.normalize.digits(work)

    @staticmethod
    def decimal_to_string(date: int) -> str:
        work = convert.decimal_to_digits(date)
        return convert.digits_to_string(work)

    @staticmethod
    def string_to_decimal(date: str, weights: list | tuple = ...) -> int:
        # NEEDS to be normalized with cc_format.normalize.string() before passing to this func
        work = convert.string_to_digits(date)
        return convert.digits_to_decimal(work, weights)


# ================ Math Class ================
class cc_math:
    """
    Docstring to be implemented\n
    -Blob
     """
    @staticmethod
    def add(dates: list[cc_date, ...] | tuple[cc_date, ...]) -> cc_date:
        """
        Adds CC Dates
        :param dates: list or tuple of cc_date
        :return:
        """
        assert len(dates) > 1
        ans = 0
        for date in dates:
            ans += date.decimal
        return cc_date(ans)

    @staticmethod
    def sub(dates: list[cc_date, ...] | tuple[cc_date, ...]) -> cc_date:
        """
        Subtracts CC Dates
        :param dates: list or tuple of cc_date
        :return:
        """
        assert len(dates) > 1
        ans = dates[0].decimal
        for date_ in dates[1:]:
            ans -= date_.decimal
        return cc_date(ans)

    @staticmethod
    def mul(dates: list[cc_date, ...] | tuple[cc_date, ...]) -> cc_date:
        """
        Multiples CC Dates
        :param dates: list or tuple of cc_date
        :return:
        """
        assert len(dates) > 1
        ans = 1
        for date_ in dates:
            ans *= date_.decimal
        return cc_date(ans)

    @staticmethod
    def div(dates: list[cc_date, ...] | tuple[cc_date, ...]) -> cc_date:
        """
        Floor Divides CC Dates
        :param dates: list or tuple of cc_date
        :return:
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

    parser.add_argument('dates', help='CC Dates', nargs='+')
    # parser.print_help()
    inp = ['-a', "!1234 ABC 123", "!1234ABC123", '(1234, 0, 1, 2, 123)', '21688812123', '(1234, 0, 1, 2, 123)']
    # args = parser.parse_args(inp)
    args = parser.parse_args()

    # Might move to cc_date class or cc_format.normalize class
    for pos, date in enumerate(args.dates):
        try:
            assert date, f"Date, {repr(date)}, must not be empty"
            # Semi safe eval.
            date = eval(date, {'__builtins__': None})

        except SyntaxError as e:
            if not cc_format.regex.findall(date):
                raise e

        except TypeError:
            raise Exception(f'{date} is not a date')

        else:
            if type(date) not in (int, list, tuple):
                raise Exception(f'{date} is invalid date format')
            args.dates[pos] = date

    if args.add:
        print(cc_math.add([cc_date(date) for date in args.dates]).string)
    elif args.sub:
        print(cc_math.sub([cc_date(date) for date in args.dates]).string)
    elif args.multiple:
        print(cc_math.mul([cc_date(date) for date in args.dates]).string)
    elif args.divide:
        print(cc_math.div([cc_date(date) for date in args.dates]).string)

    elif args.valid_formats:
        print(f'Valid Input Formats:\n'
              f'String & Decimal:\n{cc_format.valid_string_formats}\n\n'
              f'Digits:\n{cc_format.valid_digits_format}')

    elif args.convert == 'string':
        print("Dates converted to String format:")
        converted = [cc_date(date).string for date in args.dates]
        for v, c in zip(args.dates, converted):
            print(f'{v} -> {c}')

    elif args.convert == 'digits':
        print("Dates converted to Digits format:")
        converted = [cc_date(date).digits for date in args.dates]
        for v, c in zip(args.dates, converted):
            print(f'{v} -> {c}')

    elif args.convert == 'decimal':
        print("Dates converted to Decimal format:")
        converted = [cc_date(date).decimal for date in args.dates]
        for v, c in zip(args.dates, converted):
            print(f'{v} -> {c}')

    elif args.calculate == 'radix':
        print("Place value Radixes:")
        radixes = [cc_date(date).radixes for date in args.dates]
        for v, r in zip(args.dates, radixes):
            print(f'{v} -> {r}')

    elif args.calculate == 'weights':
        print("Place value Weights:")
        weights = [cc_date(date).weights for date in args.dates]
        for v, w in zip(args.dates, weights):
            print(f'{v} -> {w}')

    else:
        raise Exception("Do look at me. Argparse must of decide to go poof.")


if __name__ == '__main__':
    import sys
    cli()
    sys.exit(0)
