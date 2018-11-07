#!/usr/bin/env python3

import operator

letter = {}

for x in input().lower():
	if x in letter.keys():
		letter[x] += 1
	else:
		letter[x] = 1

# print(letter)

sorted_x = sorted(letter.items(), key=operator.itemgetter(1))

sorted_x.reverse()

for x in sorted_x:
	print(x)
