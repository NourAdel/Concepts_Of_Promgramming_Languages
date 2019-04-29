# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:28:32 2018

@author: Wahba
"""

num=int(input('enter a number: '))
factors = []
for i in range(1,num+1):
    if num%i == 0 :
        factors.append(i)
print(factors)            