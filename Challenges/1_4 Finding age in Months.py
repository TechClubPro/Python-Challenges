# -*- coding: utf-8 -*-
"""
Finding the age in months
"""

age_year = int(input("Enter your birth Year(e.g. 1983)"))
age_month = int(input("Enter your birth Year(e.g. 9 for Sept)"))

if age_month>3:
    print("Your age is " + str(((2019-age_year)*12)+(12+(3-age_month))) + " Months")
else:
    print("Your age is " + str(((2020-age_year)*12)+(3-age_month)) + " Months")
    