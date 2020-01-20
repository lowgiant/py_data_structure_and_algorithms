# -*- coding: utf-8 -*- 

sample = "one, two, one"
sample_replace_two = sample.replace("one","zero",2)
sample_replace_one = sample.replace("one","zero",1)
sample_replace_default = sample.replace("one","zero")


print("one 을 zero로 2번 변경 : " , sample_replace_two)
print("one 을 zero로 1번 변경  : " , sample_replace_one)
print("전체 다(default) 변경: " , sample_replace_default)