#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

n = 10
a = []
b = []

for i in range(0, n):
    a.append(random.randint(0, 51))

for i in range(0, n):
    if a[i] % 2 == 0:
        b.append(2 * a[i])

    if a[i] % 2 != 0:
        b.append(a[i])

b = tuple(b)

print('Massive A:', a)
print('\nKorteg B:', b)