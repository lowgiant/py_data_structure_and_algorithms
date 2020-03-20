# -*- coding: utf-8 -*- 

a = [1,2,3,]
def f(a):
    while a: 
        yield a.pop()

print(f())