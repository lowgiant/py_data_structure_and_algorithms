# -*- coding: utf-8 -*- 

import copy

#list
lists = [1,2,3,4]
list_copy = lists[:]
list_copy1 = list(lists)
print("list 슬라이싱 깊은 복사 :", list_copy, "리스트 깊은 복사 2 : ",list_copy1)

#set
people = {"홍길동", "김기수", "김기자"}
people_copy = people.copy()
people_copy.discard("홍길동")
people_copy.remove("김기수")
print("set 깊은 복사 : ",people_copy)
print("set : ", people)

#dict
name = {"이름":"홍길동"}
name_copy = name.copy()
print("딕셔너리 깊은 복사 : ", name_copy)

#str

hi = "인사"
hi_copy = copy.copy(hi)
hi_deepcopy = copy.deepcopy(hi)
print("str 얇은 카피 : ", hi_copy)
print("str 깊은 카피 : ", hi_deepcopy)

