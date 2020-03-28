# -*- coding: utf-8 -*- 
def cube(x): return x*x*x
map_test= list(map(cube,range(1,11)))

print(map_test)

seq = range(8)
def square(x): return x*x
zip_test = list(zip(seq, map(square,seq)))

print(zip_test)