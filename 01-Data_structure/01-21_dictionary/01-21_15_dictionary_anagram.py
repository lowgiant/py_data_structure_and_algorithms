# -*- coding: utf-8 -*- 

from collections import Counter

def is_anagram(s1, s2):
    counter = Counter()
    for c in s1:
        counter[c] +=1
    for c in s2:
        counter[c] -=1
    for i in counter.values():
        if i :
            return False
        return True

s1 = "marina"
s2 = "aniram"

s3 = is_anagram(s1,s2)
print(s3)

s1 = "google"
s2 = "gouglo"

s3 = is_anagram(s1,s2)
print(s3)

