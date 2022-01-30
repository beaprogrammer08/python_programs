# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:27:07 2021

@author: hp
"""

my_list=["ram","sham","ram2"]

my_list.append("hello world")
print(my_list)


my_list.insert(2,"hellooo")
print(my_list)

my_list.pop()
print(my_list)

my_list.remove("ram")
print(my_list)


my_list.sort()
print(my_list)

my_liat2=my_list.sort()
print(my_liat2)

my_list.sort(reverse=True)
print(my_list)


my_list.clear()
print(my_list)

my_list.index("ram")


del my_list[1]

print(my_list)

my_list.reverse()
print(my_list)

even=[]
odd=[]


for i in range(1,31):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)        
        
        


fibbonacci_series=[]

out=0
b=1

for i in range(0,11):
    fibbonacci_series.append(out)
    out=out+b
    b=out-b
    
print(fibbonacci_series)    






