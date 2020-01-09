# -*- coding: utf-8 -*- 

from decimal import Decimal

base = sum(0.1 for i in range(10)) == 1.0
dec = sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")

print("파이썬 기본 연산 :", base)
print("Decimal 모듈 활용 연산 :", dec)