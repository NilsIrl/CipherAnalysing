#!/usr/bin/env python3

import string
import re

def caesar(plaintext, shift):
    alphabet = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    table = str.maketrans(string.ascii_uppercase, alphabet)
    return plaintext.upper().translate(table)


frequency = [
    8.167,
    1.492,
    2.782,
    4.253,
    12.702,
    2.228,
    2.015,
    6.094,
    6.966,
    0.153,
    0.772,
    4.025,
    2.406,
    6.749,
    7.507,
    1.929,
    0.095,
    5.987,
    6.327,
    9.056,
    2.758,
    0.978,
    2.360,
    0.150,
    1.974,
    0.074,
]

textFrequency = []
results = []

text = input().upper()

letter_only_text = re.sub(r'[^A-Z]', '', text)

for y in string.ascii_uppercase:
    textFrequency.append(letter_only_text.count(y) / len(letter_only_text)
                         * 100)

for y in range(0, 25):
    error = 0.0
    for x in range(0, 25):
        error += abs(frequency[x] - textFrequency[(x + y) % 26])
    results.append(error)


shift = 26 - results.index(min(results))
print(caesar(text, shift))
print(shift)
