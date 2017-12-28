# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:28:21 2017

@author: RAY
"""

fah = float(input("Enter the temperature in Fahrenheits: "))
cel = (fah - 32) * 5 / 9
print("Equivalent temperature in Celsius: " + format(cel, '.2f'))