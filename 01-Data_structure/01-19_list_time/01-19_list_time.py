# -*- coding: utf-8 -*- 

import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def tes3():
    l = list(range(1000))

t1 = timeit.Timer()
print("concat ", t1.timeit(number=1000))    