# Use The Force

## Setup
This problem requires only Flask. To run it, run `python3 web/app.py`.

## Solution
Essentially, the program comes down to checking whether there is some pair of
characters in `str.lower()` and `str.upper()` whose difference in code point
(`ord()`) is not 0 or 32, which are the only possible results with ASCII
strings.

The solution is to input a string containing a Unicode character (the problem
title hints at UTF) whose uppercase and lowercase versions don't follow that
rule. One possible solution is the string `µ's`.
