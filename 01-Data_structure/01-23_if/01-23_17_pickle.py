# -*- coding: utf-8 -*- 
import pickle 
x= {}
x["name"] = "아스틴"
ㅌ["age"] = 23
with open("name.pkl", "wb") as f:
    pickle.dump(x,f)

with open("name.pkl","rb") as f:
    name =pickle.load(f) 

print(name)
