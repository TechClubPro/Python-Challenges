# -*- coding: utf-8 -*-
"""
Weesh Woosh Game
"""
Usernum = int(input("Enter a Number: "))
num = 0

while num<= Usernum:     
    
    if num%3 ==0 and num%5==0:
        print("Weesh Woosh")
    elif num%3==0:
        print("Weesh")
    elif num%5==0:
        print("Woosh")
    else:
        print(num)
        
    num = num+1 
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
