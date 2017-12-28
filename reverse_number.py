# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:16:50 2017

@author: RAY
"""

n = int(input("Enter a number: "))
copy = n
revnum = 0

while(copy > 0):
    dig = copy % 10
    revnum = revnum * 10 + dig
    copy = copy // 10
    
print("The reverse of " + str(n) + " is " + str(revnum) + ".")