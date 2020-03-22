# -*- coding: utf-8 -*-
"""
to find the entered character is Vowel or Consonent
"""
char = input("Please enter any character like 'a' or 'h' : ").lower()

if char in 'aeiou':
    print("Vowel")
else:
    print("Consonent")
