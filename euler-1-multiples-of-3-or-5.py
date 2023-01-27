#!/usr/bin/env python3

import sys

num = int(sys.argv[1])
total = 0
i = 0
while i < num:
  if i % 3 == 0 or i % 5 == 0:
    total = total + i
  i = i + 1

print(total)
