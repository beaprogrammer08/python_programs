# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:14:34 2021

@author: hp
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        list1=s.split(" ")
        if list1[0].isalpha()==False:
              s=list1[0]
              s=int(s)
              return(s)         
        else:
              return(0)    
sol=Solution()
sol.myAtoi("-34432 with words")
 








