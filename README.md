![Python-Ver]

# Cosmic Critter Date Format Handler <!-- omit in toc -->

<!-- TABLE OF CONTENTS -->
Table of Contents
- [Date Terminology](#date-terminology)
- [CLI Usage](#cli-usage)
  - [Help](#help)
  - [Add](#add)
  - [Subtract](#subtract)
  - [Multiple](#multiple)
  - [Divide](#divide)
  - [Convert](#convert-cli)
  - [Calculate](#calculate)
  - [Valid Formats](#valid-formats)
- [Library Usage](#library-usage)
  - [CC Format](#cc-format)
  - [CC Date](#cc-date)
  - [CC Math](#cc-math)
  - [Calc](#calc)
  - [Convert](#convert-lib)
  - [Examples](#examples)

<!-- DATE TERMINOLOGY -->
## Date Terminology

* String   - !1234 ABC 123
* Digits   - (1234, 0, 1, 2, 123)
* Decimal  - 21688812123

<!-- CLI Usage -->
## CLI Usage

For dates with Spaces use.<br>
This will be used throughout this README

**Windows**
```commandline
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

For dates without Spaces use.

**Windows**
```commandline
cc_date.py -a !1234ABC123 !4321CBA321
```

**Linux**
```commandline
python3 cc_date.py -a !1234ABC123 !4321CBA321
```

<br>

### Help

Returns help

**Windows**
```commandline
cc_date.py -h
```

**Linux**
```commandline
python3 cc_date.py -h
```

**Out**
```commandline
usage: cc_date.py [-h]
                  (-a | -s | -m | -d | -f | -c {string,digits,decimal,human} | -C {radix,weights})
                  dates [dates ...]

For use with Ivycomb's Cosmic Critters date format.

positional arguments:
  dates                 CC Date/s

options:
  -h, --help            show this help message and exit
  -a, --add             Add 2 or more CC Dates
  -s, --sub             Sub 2 or more CC Dates
  -m, --multiple        Multiple 2 or more CC Dates
  -d, --divide          Floor Divide 2 or more CC Dates
  -f, --valid-formats   Prints all valid input formats
  -c {string,digits,decimal}, --convert {string,digits,decimal}
                        Convert from String, Digits & Decimal Dates to String,
                        Digits or Decimal Dates
  -C {radix,weights}, --calculate {radix,weights}
                        Calculates the Radixes or Weights of given Date\s
```

<br>

### Add

Returns added dates. <br> dates1 + date2 + ...

**Windows**
```commandline
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```text
!5555 CCC 444
```

<br>

### Subtract

Returns subtracted dates. <br> dates1 - date2 - ...

**Windows**
```commandline
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -s "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```text
!-3088 YAB 802
```

<br>

### Multiple

Returns multiplied dates. <br> dates1 x date2 x ...

**Windows**
```commandline
cc_date.py -m "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -m "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```text
!93719058033802 LAF 483
```

<br>

### Divide

Returns floor divided dates. <br> dates1 / date2 / ...

**Windows**
```commandline
cc_date.py -d "!1234 ABC 123" "!1234 ABC 123"
```

**Linux**
```commandline
python3 cc_date.py -d "!1234 ABC 123" "1234 ABC 123"
```

**Out**

```text
!0 AAA 1
```

<br>

### Convert CLI

Convert from string, digits & decimal dates to string, digits & decimal dates
<br>Takes 1 or more dates

**Windows**
```commandline
cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321" "(1234, 0, 1, 2, 123)"
```

**Out**
```text
Dates converted to Decimal format:
!1234 ABC 123 -> 21688812123
!4321 CBA 321 -> 75947274321
(1234, 0, 1, 2, 123) -> 21688812123
```

<br>

### Calculate

Returns either the radix or weights of given dates.
<br>Takes 1 or more dates

**Windows**
```commandline
cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```commandline
python3 cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```text
Place value Radixes:
!1234 ABC 123 -> (10000, 26, 26, 26, 1000)
!4321 CBA 321 -> (10000, 26, 26, 26, 1000)
```

<br>

### Valid Formats

Returns all valid inputs. Separated by `|`.

**Windows**
```commandline
cc_date.py -f
```

**Linux**
```commandline
python3 cc_date.py -f
```

**Out**
```text
Valid Input Formats:
Strings & Decimal:
!1234 aAa 123 | !1234aAa123 
1234 aAa 123 | 1234aAa123
1234 A 123 | A 123 | 1234 A 
1234A123 | A123 | 1234A 
234123 | aAa

Digits:
[0-inf, 0-26, 0-26, 0-26, 0-999]
```

<br>

<!-- Library Usage -->
## Library Usage

### CC Date
`cc_date(date: list | tuple | str | int,
         radixes: list | tuple
         weights: list | tuple)`  
`date`: String, Digits or Decimal Date.  
`radixes`: Array of Mixed Radix; Optional.  
`weights`: Array of Weights; Optional.  

Properties:  
`.decimal` returns date as Decimal.  
`.digits` returns date as Digits.  
`.string` returns date as String.  

### CC Math
`.cc_math`

Functions:  
`.add(dates: list | tuple[cc_date, ...])` adds cc dates, returns cc date  
`.sub(dates: list | tuple[cc_date, ...])` subs cc dates, returns cc date  
`.mul(dates: list | tuple[cc_date, ...])` multiplies cc dates, returns cc date  
`.div(dates: list | tuple[cc_date, ...])` divides cc dates, returns cc date  


### CC Format
`.cc_format` Intended for internal use.

Variables:  
`.valid_string_formats` returns all valid string formats.  
`.valid_digits_format` returns valid digits format.  
`.cc_format` returns expected cc date format.  
`.regex` returns a regex to find expected date.  
`.regex_greedy` returns a regex to find valid dates & splits Year, Month & Day.

Functions:  
`.normalize.string(date: str)` used to normalize strings.  
`.normalize.digits(date: list | tuple)` used to normalize arrays.


### Calc
`.calc` Intended for internal use.

Functions:  
`.radixes(date: list | tuple)` returns tuple of the mixed radix of given date.  
`.weights(radixes: list | tuple)` returns tuple of the weights of given radixes.  


### Convert Lib
`.convert` Intended for internal use.

Functions:  
`.digits_to_decimal(date: list | tuple, weights: list | tuple = ...)`
converts digits to decimal, returns int.  
`.decimal_to_digits(date: int)` converts decimal to digits, returns tuple.  

`.digits_to_string(date: list | tuple)` converts digits to string, returns str.  
`.string_to_digits(date: str)` converts string to digits, returns tuple.  

`.decimal_to_string(date: int)` converts decimal to string, returns str.  
`.string_to_decimal(date: str, weights: list | tuple = ...)`
converts string to decimal, returns int.  


### Examples

Get date in Decimal

```python
from cc_date import cc_date

date = cc_date("!1234 ABC 123")
print(cc_date.decimal)
```

```text
21688812123
```

Add dates.

```python
from cc_date import cc_date, cc_math

date_1 = cc_date("!1234 ABC 123")
date_2 = cc_date("!4321 CBA 321")
date_3 = cc_math.add([date_1, date_2])

print(date_3.string)
```

```text
!5555 CCC 444
```

<!-- MARKDOWN LINKS & IMAGES -->
[Python-Ver]: https://img.shields.io/badge/python-3.10.6-blue?style=for-the-badge
