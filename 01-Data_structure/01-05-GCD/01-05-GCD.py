# -*- coding: utf-8 -*- 
def gcd(a,b):
    while(b != 0):
        result = b
        a, b = b, a % b
    return result

GCD = gcd(21,12)
print("최대공약수:", GCD)