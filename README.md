![Python-Ver]

# Cosmic Critter Date Format Handler <!-- omit in toc -->

<!-- TABLE OF CONTENTS -->
### Table of Contents
- [Date Terminology](#date-terminology)
- [Format](#format)
- [CLI Usage](#cli-usage)
  - [Help](#help)
  - [Clean Out](#clean-out)
  - [Add](#add)
  - [Subtract](#subtract)
  - [Multiple](#multiple)
  - [Divide](#divide)
  - [Convert CLI](#convert-cli)
  - [Calculate](#calculate)
  - [Normalize CLI](#normalize-cli)
  - [Valid Formats](#valid-formats)
- [Library Usage](#library-usage)
  - [CC Date](#cc-date)
  - [CC Math](#cc-math)
  - [CC Format](#cc-format)
  - [Normalize Lib](#normalize-lib)
  - [Calc](#calc)
  - [Convert Lib](#convert-lib)
  - [Examples](#examples)

<!-- DATE TERMINOLOGY -->
## Date Terminology

* String   - !1234 ABC 123
* Digits   - (1234, 0, 1, 2, 123)
* Decimal  - 21688812123

## Format
Cosmic Critters (CC) format is: `!YYYY MMM DDD`, `!0-inf A-Z*3 0-999`  
*It's unknown what CC Dates represent. Year, Month & Day are placeholders*
* String is in CC format
* Digits is the letters converted their numbers in base26
* Decimal is the date converted down to Days

<!-- CLI Usage -->
## CLI Usage

For dates with Spaces use.<br>
This will be used throughout this README

**Windows**
```
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

For dates without Spaces use.

**Windows**
```
cc_date.py -a !1234ABC123 !4321CBA321
```

**Linux**
```
python3 cc_date.py -a !1234ABC123 !4321CBA321
```

<br>

### Help

Returns help

**Windows**
```
cc_date.py -h
```

**Linux**
```
python3 cc_date.py -h
```

**Out**
```
usage: cc_date.py [-h] [--cleanout]
                  (-a | -s | -m | -d | -f | -c {string,digits,decimal} | -C {radix,weights} | -n {string,digits})
                  dates [dates ...]

For use with Ivycomb's Cosmic Critters date format.

positional arguments:
  dates                 CC Dates

options:
  -h, --help            show this help message and exit
  --cleanout            Makes output clean for easier copying.
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
  -n {string,digits}, --normalize {string,digits}
                        Normalize strings & arrays to expected formats. Script
                        does this automatically.
```

<br>

### Clean Out

Makes output clean for easier copying.

**Windows**
```
cc_date.py --cleanout [arguments]
```

**Linux**
```
python3 cc_date.py --cleanout [arguments]
```

<br>

### Add

Returns added dates. <br> dates1 + date2 + ...

**Windows**
```
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```
!5555 CCC 444
```

<br>

### Subtract

Returns subtracted dates. <br> dates1 - date2 - ...

**Windows**
```
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -s "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```
!-3088 YAB 802
```

<br>

### Multiple

Returns multiplied dates. <br> dates1 * date2 * ...

**Windows**
```
cc_date.py -m "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -m "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```
!93719058033802 LAF 483
```

<br>

### Divide

Returns floor divided dates. <br> dates1 // date2 // ...

**Windows**
```
cc_date.py -d "!1234 ABC 123" "!1234 ABC 123"
```

**Linux**
```
python3 cc_date.py -d "!1234 ABC 123" "1234 ABC 123"
```

**Out**

```
!0 AAA 1
```

<br>

### Convert CLI

Convert from string, digits & decimal dates to string, digits & decimal dates
<br>Takes 1 or more dates

**Windows**
```
cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321" "(1234, 0, 1, 2, 123)"
```

**Out**
```
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
```
cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```

**Linux**
```
python3 cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```

**Out**
```
Place value Radixes:
!1234 ABC 123 -> (10000, 26, 26, 26, 1000)
!4321 CBA 321 -> (10000, 26, 26, 26, 1000)
```

<br>

### Normalize CLI

Normalize strings & arrays to expected formats. Script does this automatically.

**Windows**
```
cc_date.py -n string !14ABC13 '1234 A123'
```

**Linux**
```
python3 cc_date.py -n string !14ABC13 '1234 A123'
```

**Out**
```
String Dates Normalized:
!14ABC13 -> !14 ABC 013
1234 A123 -> !1234 AAA 123
```

<br>

### Valid Formats

Returns all valid inputs. Separated by `|`.

**Windows**
```
cc_date.py -f
```

**Linux**
```
python3 cc_date.py -f
```

**Out**
```
Valid Input Formats:
Strings & Decimal:
!1234 aAa 123 | !1234aAa123 
1234 aAa 123 | 1234aAa123
1234 A 123 | A 123 | 1234 A 
1234A123 | A123 | 1234A 
234123 | aAa

Digits:
[0-inf, 0-25, 0-25, 0-25, 0-999]
(0-inf, 0-25, 0-25, 0-25, 0-999)
```

<br>

<!-- Library Usage -->
## Library Usage

### CC Date
`cc_date(date: list[int] | tuple[int, ...] | str | int,
         radixes: list[int]
         weights: list[int])`  
`date`: String, Digits or Decimal Date.  
`radixes`: Array of Mixed Radix; Optional.  
`weights`: Array of Weights; Optional.  

Properties:  
`.decimal` returns date as Decimal.  
`.digits` returns date as Digits.  
`.string` returns date as String.  

### CC Math
`cc_math`

Functions:  
`.add(dates: list[cc_date])` adds cc dates, returns cc date  
`.sub(dates: list[cc_date])` subs cc dates, returns cc date  
`.mul(dates: list[cc_date])` multiplies cc dates, returns cc date  
`.div(dates: list[cc_date])` divides cc dates, returns cc date  


### CC Format
`cc_format` Intended for internal use.

Variables:  
`.valid_string_formats` all valid string formats.  
`.valid_digits_format` all valid digits format.  
`.cc_format` example cc date format.  
`.regex` a regex to find expected date.  
`.regex_greedy` a regex to find valid dates & splits Year, Month & Day.


### Normalize Lib
`normalize` Intended for internal use. Used to normalize.

Functions:  
`.string(date: str)` used to normalize strings.  
`.digits(date: list[int] | tuple[int, ...])` used to normalize lists.


### Calc
`calc` Intended for internal use.

Functions:  
`.radixes(date: list[int])` returns list of the mixed radix of given date.  
`.weights(radixes: list[int])` returns list of the weights of given radixes.  


### Convert Lib
`convert` Intended for internal use.

Functions:  
`.digits_to_decimal(date: list[int], weights: list[int] = ...)`
converts digits to decimal, returns int.  
`.decimal_to_digits(date: int)` converts decimal to digits, returns list.  

`.digits_to_string(date: list[int])` converts digits to string, returns str.  
`.string_to_digits(date: str)` converts string to digits, returns list.  

`.decimal_to_string(date: int)` converts decimal to string, returns str.  
`.string_to_decimal(date: str, weights: list[int] = ...)`
converts string to decimal, returns int.  


### Examples

Get String in Decimal date

```python
from cc_date import cc_date

date = cc_date("!1234 ABC 123")
print(cc_date.decimal)
```

```
21688812123
```

Convert Decimal to String date

```python
from cc_date import cc_date
date = cc_date(21688812123)
print(cc_date.string)
```

```
!1234 ABC 123
```

Add dates.

```python
from cc_date import cc_date, cc_math

date_1 = cc_date("!1234 ABC 123")
date_2 = cc_date("!4321 CBA 321")
date_3 = cc_math.add([date_1, date_2])

print(date_3.string)
```

```
!5555 CCC 444
```

<!-- MARKDOWN LINKS & IMAGES -->
[Python-Ver]: https://img.shields.io/badge/python-3.10.6-blue?style=for-the-badge
