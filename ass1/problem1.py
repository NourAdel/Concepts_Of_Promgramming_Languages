# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x= int (input())
i=0
l=[]
while i< (x):
   y=int (input())
   l.insert(i,y)
   i=i+1
  
ind=int(input())
l.sort(reverse=True)
print (l[x-ind])   
   
    