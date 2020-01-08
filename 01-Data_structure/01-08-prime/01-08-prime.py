# -*- coding: utf-8 -*- 

import math 
import random

yes = "소수"
no = "정수"

def brute_prime(number):
    num = abs(number)
    if num < 4 : return yes
    for x in range(2, num):
        if num % x == 0:
            return no
        return yes

def sqrt_prime(number):
    num = abs(number)
    if num < 4 : return yes
    for x in range(2, int(math.sqrt(num))+1):
        if number % x == 0:
            return no
    return yes

def fermat_prime(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number - 1, number) != 1:
                return no
        return yes
    else:
        for a in range(100):
            a = random.randint(2, number -1)
            if pow(a ,number, -1, number) != 1:
                return no
        return yes

def test_prime():
    number1 = 17
    number2 = 20
    brute1 = brute_prime(number1)
    print("'17' 소수확인, 브루트 방식:", brute1)
    brute2 = brute_prime(number2)
    print("'20' 소수확인, 브루트 방식:", brute2)
    sqrt1 = sqrt_prime(number1)
    print("'17' 소수확인, 제곱근 방식:", sqrt1)
    sqrt2 = sqrt_prime(number2)    
    print("'20' 소수확인, 제곱근 방식:", sqrt2)
    fermat1 = fermat_prime(number1)
    print("'17' 소수확인, 페르마 방식:", fermat1)
    fermat2 = fermat_prime(number2)
    print("'20' 소수확인, 페르마 방식:", fermat2)
    return None

print(test_prime())