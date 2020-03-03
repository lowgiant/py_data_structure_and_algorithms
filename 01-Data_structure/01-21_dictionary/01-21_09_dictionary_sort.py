# -*- coding: utf-8 -*- 

d = dict(b= "게임",c ="난장판",a= "청소")

print("딕셔너리 키를 기준으로 순회")
for key in sorted(d.keys()):
    print(key,d[key])

