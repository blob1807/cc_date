![Python-Ver]

# Cosmic Critter Date Format Handler


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#date-terminology">Date Terminology</a></li>
    <li>
        <a href="#cli-usage">CLI Usage</a>
        <ul>
            <li><a href="#help">Help</a></li>
            <li><a href="#add">Add</a></li>
            <li><a href="#subtract">Subtract</a></li>
            <li><a href="#multiple">Multiple</a></li>
            <li><a href="#divide">Divide</a></li>
            <li><a href="#valid-formats">Valid Formats</a></li>
            <li><a href="#convert">Convert</a></li>
            <li><a href="#calculate">Calculate</a></li>
        </ul>
    </li>
    <li>
        <a href="#library-usage">Library Usage</a>
        <ul>
            <li><a href="#exaples">Examples</a> </li>
        </ul>
    </li>
  </ol>
</details>



<!-- DATE TERMINOLOGY -->
## Date Terminology
* String   - !1234 ABC 123
* Digits   - (1234, 0, 1, 2, 123)
* Decimal  - 21688812123
* Human    - 2657-04-16 22:02:03



<!-- CLI Usage -->
## CLI Usage

For dates with Spaces use.<br>
This will be used throughout this README

*Windows*
```commandline
cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

*Linux*
```commandline
python3 cc_date.py -a "!1234 ABC 123" "!4321 CBA 321"
```

For dates without Spaces use.

*Windows*
```commandline
cc_date.py -a !1234ABC123 !4321CBA321
```

*Linux*
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
```
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
  -d, --divide          Divide 2 or more CC Dates
  -f, --valid-formats   Prints all valid input formats
  -c {string,digits,decimal,human}, --convert {string,digits,decimal,human}
                        Convert from String, Digits & Decimal Dates to String,
                        Digits, Decimal or Human Dates
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
```
!!5555 CCC 444
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
```
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
```
!93719058033802 LAF 483
```
<br>

### Divide
Returns floor divided dates. <br> dates1 / date2 / ...

**Windows**
```commandline
cc_date.py -d "!1234 ABC 123" "!4321 CBA 321"
```
**Linux**
```commandline
python3 cc_date.py -d "!1234 ABC 123" "!4321 CBA 321"
```
**Out**
```
!0 AAA 0
```
<br>

### Convert
Convert from string, digits & decimal dates to string, digits, decimal & human dates

**Windows**
```commandline
cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321"
```
**Linux**
```commandline
python3 cc_date.py -c decimal "!1234 ABC 123" "!4321 CBA 321"
```
**Out**
```
Date\s converted to Decimal format:
!1234 ABC 123 -> 21688812123
!4321 CBA 321 -> 75947274321
```
<br>

### Calculate
Returns either the radix or weights of given dates.

**Windows**
```commandline
cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```
**Linux**
```commandline
python3 cc_date.py -C radix "!1234 ABC 123" "!4321 CBA 321"
```
**Out**
```
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
```
Valid Input Formats:
Strings & Decimal:
!1234 aAa 123 | !1234aAa123 
1234 aAa 123 | 1234aAa123
1234 A 123 | A 123 | 1234 A 
1234A123 | A123 | 1234A 
234123 | aAa

Digits:
[0-inf, 0-26, 0-26, 0-26, ..., 0-999]
```
<br>



<!-- Library Usage -->
## Library Usage
Coming Soon.<br>
For now just look at the `cli()` func, docstrings & comments on how to use it.

### Examples
Get date in Decimal
```python
from cc_date import cc_date

date = cc_date("!1234 ABC 123")
print(cc_date.decimal)
```
```pycon
21688812123
```
<br>

Add dates.

```python
from cc_date import cc_date, cc_math

date_1 = cc_date("!1234 ABC 123")
date_2 = cc_date("!4321 CBA 321")
date_3 = cc_math.add([date_1, date_2])

print(date_3.string)
```
```pycon
!5555 CCC 444
```
<br>

Convert CC Date to Human Date
```python
from cc_date import cc_date
from datetime import datetime

date = cc_date("!1234 ABC 123")
print(datetime.fromtimestamp(date.decimal))
```
```pycon
2657-04-16 22:02:03
```

<!-- MARKDOWN LINKS & IMAGES -->
[Python-Ver]: https://img.shields.io/badge/python-3.10.x-blue?style=for-the-badge