# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:34:29 2018

@author: Wahba
"""


print('Enter number')
num = input()
print("Enter number's base")
fromBase = input()
print('convert it to base')
toBase = input()
decimal=0
x = len(num)-1
for i in range (len(num)):
    decimal = decimal + int(num[i])*(int(fromBase)**x)
    x = x - 1
new_num = ""
dev = decimal
while dev !=0 :
    remender = dev % int(toBase)
    dev = dev // int(toBase)
    new_num = str(remender) + new_num
print( new_num)
