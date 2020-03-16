userNum = 0
calcNum = 0
UpLimit = 1000
LowLimit =0
step =0

while userNum != "=":
    step = step + 1
    
    calcNum = int((UpLimit+LowLimit)/2)
    userNum = input("Is your Num : " + str(calcNum) + " ")
    
    if userNum=='<':
        UpLimit = calcNum    

    if userNum=='>':
        LowLimit = calcNum

print("Got the number in " + str(step) + " Steps")










