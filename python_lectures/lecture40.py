# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:37:29 2021

@author: hp
"""
# list comperhension


my_list=[10,20,30,40,50]
my_list1=[]
for i in my_list:
    my_list1.append(i*2)
print(my_list1)


my_list=[10,20,30,40,50]
out=[i*2 for i in my_list]
print(out)



my_list=[5,10,15,20,30,40,50]
out=[i*2 for i in my_list if i%2==0]
print(out)



my_list=[1,2,3,4,5]
out={i:i**2 for i in my_list}
print(out)


    