# -*- coding: utf-8 -*- 

import itertools

def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i , c in enumerate(s):
        for cc in perm(s[:i ]+ s[i+1:]):
            res.append(c+cc)
    return res

def perm2(s):
    res = itertools.permutations(s)
    return ["".join(i) for i in res]

val = "012"
print("문자열 순열 :",  perm(val))
print("문자열 순열 모듈 사용:",perm2(val))