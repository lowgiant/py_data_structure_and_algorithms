# -*- coding: utf-8 -*- 
import collections

Person = collections.namedtuple('Person', 'name age gender')

p = Person('아스틴', '30', '남자')
print("네임드 튜플 : ", p)