# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:45:14 2021

@author: hp
"""

my_list=["ram","sham","rahul",["replave","hfejcn"]]
my_list.append(["sunil","sham"])
print(my_list)

my_list=["ram","sham","rahul"]
my_list.extend(["sunil","sham"])
print(my_list)



my_string="my name is dupesh"
my_list=my_string.split()
print(my_list)

my_list1=my_list[0]+my_list[1]
print(my_list1)


my_list=["my","is","dupesh"]
my_string=" ".join(my_list)
print(my_string)




my_list=["dupeshbansal08@gmail.com","helloworld12@gmail.com","ram123@gmail.com"]
my_string=' '.join(my_list)
print(my_string)
name=my_string.split("@gmail.com")
print(name)
my_list1=my_string.split("@")
my_string1=" ".join(my_list1)
print(my_string1)


my_list=["dupeshbansal08@gmail.com","helloworld12@gmail.com","ram123@gmail.com"]
gmail_list=[]
name_list=[]
for item in my_list:
    print(item)
    name=item.split("@")
    print(name)
    names=name[0]
    name_list.append(names)
    print(name_list)                
    gmail=name[1]
    gmail_list.append(gmail)
    print(gmail_list)


my_list=[1,2,3,4]
for item in my_list:
    print(item,end="") 
    item=str(item)
    item=int(item)
a=item+1
print(a)


my_list=[1,2,["ram","sham"]]
my_list[2][0]
my_list[2][1][2]


my_string=1234
my_string1=my_string+1
print(my_string1)





































































         