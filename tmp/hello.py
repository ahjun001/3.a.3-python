#!/usr/bin/env python3

import sys

print(f"{sys.argv=}", end="\n\n")

if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        print(f"Hello {sys.argv[i]}")
else:
    print("Hello Python world")
