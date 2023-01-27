#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
total1 = 0
total2 = 0

i = 0
while i < n:
  total1 = total1 + (i + 1)
  i = i + 1

i = 0
while i < n:
  total2 = total2 + ((i + 1) ** 2)
  i = i + 1

print((total1 ** 2) - total2)
