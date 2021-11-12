#!/usr/bin/env python3

import math
import os

os.system("clear")

# simple use of variables
name = "Peter"
age = 23
print(f"{name} is {age} years old.\n")

#  self-documenting = within f-string, mostly for debug strings
print(f"{(y := .5) = :.2f}\n")

x = 0.8
print(f"{math.cos(x) = }")
print(f"{math.sin(x) = }")
print()

# using simple format specifier with self-documenting =
print(f"{math.pi = :.2f}")
print()

# f-string containing an expression
bags = 2
appples_in_bag = 12
print(f"There are total of {bags * appples_in_bag} apples.\n")

# works with dictionaries
folks = {"John": 22, "Mary": 20, "Junior": 3}
for key, val in folks.items():
    print(f"{key} is {val}")
print()

# multiline f-string
name = "John"
age = 23
weight = 75.555
msg = (
    f"{name = }\n"
    f"{age = }\n"
    f"{weight = :.1f}\n"
    f"{name = }\n"
    f"{age = }\n"
    f"{weight = :.1f}\n"
)
print(msg, "\n")

# escape characters
print(f"Python uses {{}} to evaluate variables in f-strings")
print(f"' escapes with \\, as in \\', but black does not keep them")
print()

# f-string format width
for x in range(0, 11, 5):
    print(f"{x:2} {x**2:03} {x**3:4}")
print()


# f-string f format alignment
for n in range(1, 4):
    print(f"{n = }\t{math.pi**n = :5.2f}\t{math.pi**n**n = :20.3f}")
print()


# right justified strings of a set length
s = ("a", "ab", "abc", "abcd")
for _ in range(len(s)):
    print(f"{s[_]:>4}")
