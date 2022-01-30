# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:07:06 2021

@author: hp
"""

        

i=input("enter the number:")
i=int(i)
out=0
for item in range(1,i+1):
    item=str(item)
    b=item.count("1")
    out=out+b
print(out)
    


my_tup="ram",4653
type(my_tup)



my_list=[1,2,3,4]
my_list1=[]
my_list2=[]
for item in my_list:
     my_list1.append(str(item))
my_string="".join(my_list1)
my_string=int(my_string)
my_string1=my_string+1   
my_string1=str(my_string1)
for number in my_string1:
        my_list2.append(int(number))
print(my_list2)        





my_list=[9,9,9]
my_list1=[]
my_list2=[]
for item in my_list:
     my_list1.append(str(item))
print(my_list1)     

my_string="".join(my_list1)
my_string=int(my_string)
print(my_string) 
my_string1=my_string+1   
print(my_string1) 
my_string1=str(my_string1)
for number in my_string1:
        my_list2.append(int(number))
print(my_list2)        

















my_list=[2343454657,8,7,9]
my_list1=[]
my_list2=[]
for item in my_list:
     my_list1.append(str(item))
my_string="".join(my_list1)
my_string=int(my_string)
my_string1=my_string+1   
my_string1=str(my_string1)
for number in my_string1:
        my_list2.append(int(number))
print(my_list2)        
