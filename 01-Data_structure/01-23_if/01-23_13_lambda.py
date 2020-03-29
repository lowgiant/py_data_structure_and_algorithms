# -*- coding: utf-8 -*- 

def area(b,h):
    return 0.5 * b*h

area_s= area(5,4)

print(area_s)

area_lam = lambda b, h: 0.5 * b *h
area_l= area_lam(5,4)

print(area_l)