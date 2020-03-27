# -*- coding: utf-8 -*- 
def f(x): return x % 2 !=0 and x %3 != 0

print("if 문으로 구현:",f(17))

f_rest = list(filter(f, range(2,25)))
print("filter를 활용해서 정리 :",f_rest)