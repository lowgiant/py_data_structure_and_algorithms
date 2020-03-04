# -*- coding: utf-8 -*- 

def hello():
    print("Hi")

def world():
    print("Korea")

action = "h"

#딕셔버리 값으로 함수 호출
functions = dict(h=hello, w=world)
functions["w"]()

#리스트 값 추가해서 확인
he = ["h","w"]

for i in he:
    functions[i]()