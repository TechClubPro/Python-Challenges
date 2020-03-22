# -*- coding: utf-8 -*-
"""
Program to find the largest among the 3 numbers
"""

largestNum=0

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))


if num1 >= num2 and num1 >= num3:
    largestNum = num1
elif num2 >= num1 and num2 >= num3:
    largestNum = num2
else:
    largestNum = num3

print("The Largset number among "+ str(num1) + ", "+str(num2) + " and " + str(num3) + " is "+ str(largestNum)+"! ")
