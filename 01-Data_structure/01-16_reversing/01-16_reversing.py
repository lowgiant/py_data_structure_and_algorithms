# -*- coding: utf-8 -*- 

def revert(f):
    if f:
        f = f[-1] + revert(f[:-1])
    return f

def revert2(f):
    return f[::-1]

sample1 = "안녕하세요!"
sample2 = "어서오세요."


print("1번째 샘플 전환")
print(revert(sample1))
print(revert2(sample1))

print("2번째 샘플 전환")
print(revert(sample2))
print(revert2(sample2))
