#!/usr/bin/env python3
import math

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
print(sorted([data[x] for x in range(len(data))], key=abs))

# Выводит первыми отрицательные числа
#print(sorted([data[x] for x in range(len(data))], key=lambda n: (abs(-n), n)))
