# -*- coding: utf-8 -*- 

def append(number, number_list=None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    return number_list

print("리스트 5 추가:", append(5))
print("리스트 7 추가:", append(7))
print("리스트 2 추가:", append(2))
