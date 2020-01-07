# -*- coding: utf-8 -*- 
def fibo_seq(n):
    if n < 2: return n
    a , b = 0, 1
    for i in range(n):
        a, b =b, a+b
    return a

fibo = fibo_seq(10)

print("10까지 피보나치 수열: ", fibo)