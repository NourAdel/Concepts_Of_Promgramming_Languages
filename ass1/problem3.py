# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:31:33 2018

@author: Wahba
"""

print('Enter your interval')
bgn=int(input())
end=int(input())
Armsttrong_arr = []
for i in range(bgn,end+1):
    stri = str(i)
    sum = 0
    for j in range (len(stri)):
        sum=sum+int(stri[j])**len(stri)
    if sum == i :
            Armsttrong_arr.append(i)
print( Armsttrong_arr)