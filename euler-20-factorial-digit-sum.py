#!/usr/bin/env python3

import sys
total = []
n = int(sys.argv[1])

i = 0
while i < n:
  total.append(n - i)
  i = i + 1

if n != 0:
  newtotal = total[0]
else:
  newtotal = 0

i = 1
while i < len(total):
  newtotal = newtotal * total[i]
  i = i + 1

newtotal = str(newtotal)
finaltotal = 0
i = 0
while i < len(newtotal):
  finaltotal = finaltotal + int(newtotal[i])
  i = i + 1

print(finaltotal)
