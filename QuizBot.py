""" Program for QuizBot """

Qnum=1
Score=0

while Qnum<=5:
    
    if Qnum==1:
        
        print("Corona Virus started in which city?")
        print("A:Wihan B:Shanghai C:Wuhan D:Beijing ")
       
        ans = input("Whats your Answer A B C D : ")
        
        if ans =='c' or ans == 'C':
            print("Correct Ans !")
            Score = Score + 1
            print(Score)
        else:
            print("Wrong Ans")
            print(Score)
            
    if Qnum==2:
        
        print("Who is the President of US ")
        print("A:Mr Spade B:Mr Trump C:Mr Clinton D:Mr Bush ")
        
        ans = input("Whats your Answer A B C D : ")
        
        if ans =='B' or ans == 'b':
            print("Correct Ans !")
            Score = Score + 1
            print(Score)
        else:
            print("Wrong Ans")
            print(Score)
            
    if Qnum==3:
        
        print("What's the cube of 17 ? ")
        print("A:2007 B:54248 C:8574 D:4913 ")
        
        ans = input("Whats your Answer A B C D: ")
        
        if ans =='D' or ans == 'd':
            print("Correct Ans !")
            Score = Score + 1
            print(Score)
        else:
            print("Wrong Ans")
            print(Score)
    
    if Qnum==4:
        
        print("Where is CharMinar situated? ")
        print("A:Hyderabad B:Delhi C:Pune D:Banglore ")
        
        ans = input("Whats your Answer A B C D: ")
        if ans =='A' or ans == 'a':
            print("Correct Ans !")
            Score = Score + 1
            print(Score)
        else:
            print("Wrong Ans")
            print(Score)
    
    if Qnum==5:
        
        print("National Bird of India ? ")
        print("A:Hen B:PeaCock C:Pigeon  D:Cat ")
        ans = input("Whats your Answer A B C D: ")
        if ans =='B' or ans == 'b':
            print("Correct Ans !")
            Score = Score + 1
            print(Score)
        else:
            print("Wrong Ans")
            print(Score)
    Qnum = Qnum + 1
    
if Score < 3:
    print("You need to stop playing Mobile Games") 
elif Score == 3:
    print("Thik ha bhai !!")
elif Score == 4:
    print("Good !!")
elif Score == 5:
    print("Is Einstien your Classmate? ")     