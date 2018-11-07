#!/usr/bin/env python3

import string

inStr = input().lower()
move = int(input())
result = ""

if input() == "True":
	inStr = inStr[::-1]

for x in inStr:
	place = None
	for y in range(len(string.ascii_lowercase)):
		if x == string.ascii_lowercase[y]:
			place = y
			if y + move >= 26:
				result += string.ascii_lowercase[move-(26-y)]
			else:
				result += string.ascii_lowercase[y+move]
			break

		elif y == 25:
			result += x

print(result)
