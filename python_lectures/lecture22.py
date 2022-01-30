# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:45:16 2021

@author: hp
"""

# sets 
my_set=set()
print(my_set)

my_set={"ram",23,223.23,True,("ram",)}
print(my_set)#no index value

my_set={6513}
print(my_set)


my_set={6513.6565}
print(my_set)


my_set={("erah",)}
print(my_set)



my_set={[24,35]}
print(my_set)




my_set={{"ran":213},{"rang":2613}}
print(my_set)


my_set={True}
print(my_set)


my_set={{6513}}
print(my_set)


#sets are mutable
#sets are unordered collection of data types and are unique 




my_set={"ram",23,223.23,True,("ram",),"ram"}
print(my_set)#always print unique value






my_list=[2,1,1,2,3]
my_set=set(my_list)
my_list=list(my_set)
print(my_list)








my_list=["ram","sham","rahul"]
my_list1=["ram","vikas"]
my_set=set(my_list)
my_set1=set(my_list1)
my_set.union(my_set1)
my_set.intersection(my_set1)
my_set.symmetric_difference(my_set1)  
my_set.difference(my_set1) 
my_set1.difference(my_set)



my_set={"jmhn","ram","thwgdf"}
my_set.pop()












my_set={"7jrge","QT$"}
my_set.add("khj,jgmkgm")
print(my_set)
my_set1=frozenset(my_set)
print(my_set1)
my_set1.add("jhgbm")
print(my_set1)


my_set1.__len__()
my_list=["1",7,["676"],{1:1,2:4}]
my_list[3][1]






