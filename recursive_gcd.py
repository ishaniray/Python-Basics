# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:42:48 2017

@author: RAY
"""

def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))

hcf = gcd(a, b)

print("\nThe GCD of " + str(a) + " and " + str(b) + " is " + str(hcf) + ".")