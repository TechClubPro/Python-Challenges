# -*- coding: utf-8 -*-
"""
Program to find the Type of Triangle
1. Equilateral : All sides are equal
2. Isosceles : 2 sides are equal
3. Scalene : No sides are equal
"""
side1 = int(input("Enter the dimension of 1st side : "))
side2 = int(input("Enter the dimension of 2nd side : "))
side3 = int(input("Enter the dimension of 3rd side : "))

if side1 == side2 and side1 == side3:
    print("Triangle is Equilateral")
elif side1 != side2 and side1 != side3 and side2 != side3:
    print("Triangle is Scalene ")
else:
    print("Triangle is Isosceles")
