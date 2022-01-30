# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:40:05 2021

@author: hp
"""


# Matrice program


i=input("enter the rows:-")
i=int(i)
j=input("enter the column:-")
j=int(j)
my_list=[]
my_list1=[]
for a in range(1,j+1):
    my_list.append(a)

for item in range(0,i):
     my_list1.append(my_list)
print(my_list1)    
    
    


     

i=input("enter the number:-")
i=int(i)
my_list_1=[1,2]
my_list=[]
for item in range(0,i):
    my_list.append(my_list_1)
print(my_list,"\n")
        


i=input("enter the rows:-")
i=int(i)
j=input("enter the column:-")
j=int(j)
my_list=[]
my_list1=[]
out=0
for item in range(0,i): 
    for a in range(0,j):
        out+=1
        my_list.append(out)
    my_list1.append(my_list) 
print(my_list1)    
    
    
     
    
    
    
    
i=int(input("enter the row :"))
j=int(input("enter the column :"))   

my_list1=[]
out=1
for item in range(0,i):
    my_list=[]
    for a in range(0,j):
        my_list.append(out)
        out=out+1
    my_list1.append(my_list)    
       
print(my_list1)    




try:
    out=[]
    count=1
    c=int(input("enter the column:"))
    r=int(input("enter the row:"))

    for j in range(0,r):
        row=[]
        for i in range(0,c):
            row.append(count)
            count+=1
        out.append(row)    
    print(out)
except:
    print("error")
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    