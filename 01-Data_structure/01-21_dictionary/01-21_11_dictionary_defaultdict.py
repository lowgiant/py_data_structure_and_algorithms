# -*- coding: utf-8 -*- 

from collections import defaultdict

def default_ex():
    pairs = {("a", 1), ("b", 2), ("c",3)}

    #일반 딕셔너리
    d1 = {}
    for key, value in pairs:
        if key not in d1: 
            d1[key] = []
        d1[key].append(value)
    print(d1)
    
    d2 = defaultdict(list)
    for key, value in pairs:
        d2[key].append(value)
    print(d2)

default_ex()