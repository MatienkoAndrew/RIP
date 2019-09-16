#!/usr/bin/env python3
import math

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
def is_module(x):
    if x < 0:
        return 0
    else:
        return 1

# for i in range(len(data)):
#     data[i] = is_module(data[i])
#     print(data[i])
print(sorted([data[x] for x in range(len(data)) if is_module(data[x])]))