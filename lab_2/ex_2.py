#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 3, 4, 4, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
# print(list(data2))
a = Unique(data1)
for i in a:
    if i != None:
        print(i)

data = ['a', 'B', 'A', 'b']
c = Unique(data)
for i in c:
    if i != None:
        print(i)