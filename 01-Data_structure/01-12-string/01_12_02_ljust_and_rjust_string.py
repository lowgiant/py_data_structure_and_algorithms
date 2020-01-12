# -*- coding: utf-8 -*- 

hi_str = "안녕하세요."
rjust_str = hi_str.rjust(10, '-')
ljust_str = hi_str.ljust(10, '-')

print("문자열 왼쪽으로 10에서 남은 길이 만큼 - 추가 : ",rjust_str)
print("문자열 오른쪽으로 10에서 남은 길이 만큼 - 추가 : ", ljust_str)