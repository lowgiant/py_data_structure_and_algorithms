# -*- coding: utf-8 -*- 

hi = "{0} {1}".format("안녕", "하세요." )
print("format 필드인덱스 0 부터 시작: ", hi)

personal_data_version1 = "이름:{name}, 나이:{age}".format(name = "홍길동", age = "30")
print("변수명으로 기입 가능 : ",personal_data_version1) 

personal_data_version2 = "이름:{name}, 나이:{0}".format(30, name = "홍길동")
print("변수명 + 필드인덱스으로 기입 가능 : ",personal_data_version2) 

personal_data_version3 = "이름:{}, 나이:{}".format("홍길동",30)
print("인덱스 생략 가능 : ",personal_data_version3) 
