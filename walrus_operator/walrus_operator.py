#!/usr/bin/env python3

# traditional
n = len([1, 2, 3])
if n > 1:
    print(f"list is {n} chars long")

# using walrus :=  (that looks like a walrus sideways)
if (m := len([1, 2])) > 1:
    print(f"list is {m} chars long")
