# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:01:29 2018

@author: Wahba
"""


class nibble:

    def __init__(self, val):
        self.vs = val
        self.v = int(val)
        self.bits = []

    def tobin(self):
        self.bits = format(self.v, 'b')
        i = len(self.bits)
        if (i < 4):
            y = 4 - i
            while (y > 0):
                t = '0' + self.bits
                self.bits = t
                i = i + 1
                y = y - 1

class BCDN:


    def __init__(self, s):
        self.counter = len(s)
        self.ns = []
        i = 0
        while (i < len(s)):
            m = nibble(int(s[i]))
            m.tobin()
            self.ns.append(m)
            i = i + 1


def fix(x=BCDN, y=BCDN):
    if (x.counter != y.counter):
        if (x.counter > y.counter):
            smaller = y
            bigger = x
        else:
            smaller = x
            bigger = y
        while (smaller.counter != bigger.counter):
            m = nibble('0')
            m.tobin()
            smaller.ns.insert(0, m)
            smaller.counter = smaller.counter + 1


def binaryadd(x=nibble, y=nibble, w=int):
    result = ""
    carry = w
    flag = False
    for i in range(len(x.bits)-1, -1, -1):
        r = carry
        r += 1 if x.bits[i] == '1' else 0
        r += 1 if y.bits[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    ' '.join(format(ord(x), 'b') for x in result)
    t = int(result, 2)
    if t > 9:
        flag = True    
    return result, carry, flag


def BCDadder(x=BCDN, y=BCDN):
    six = nibble('6')
    six.tobin()
    result = []
    c = 0
    num=''
    fix(x, y)
    for i in range(x.counter-1, -1,-1):
        tem = binaryadd(x.ns[i], y.ns[i], c)
        c = tem[1]
        if (tem[2] or c == 1):
            ' '.join(format(ord(x), 'b') for x in tem[0])
            t = int(tem[0], 2)
            t = str(t)
            tt = nibble(t)
            tt.tobin()
            tem2 = binaryadd(six, tt, 0)
        else:
            tem2 = tem
            c=tem[1]
            
        result.append(tem2[0])  
    if (c == 1):
        result.append('0001')
    result.reverse()
    for i in range(len(result)):
        ' '.join(format(ord(x), 'b') for x in result[i])
        x=int (result[i],2)
        num=num+str(x)
        
    return (num)


n = input('Enter the first number: ' )
x=BCDN(n)
m= input('Enter the second number: ' )
y=BCDN(m)
s = BCDadder(x, y)
print(s)
