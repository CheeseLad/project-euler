#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
prev = 0
curr = 1
total = 0
i = 0
while prev < n:
  if prev % 2 == 0:
    total = total + prev
  tmp = curr
  curr = curr + prev
  prev = tmp
  i = i + 1

print(total)
