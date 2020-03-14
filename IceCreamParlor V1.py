price =0
done=0

print("Welcome to SpyNav IceCream Shop")
print("Choose your Flavor")
print("1. ChocoChips  Rs 75/-")
print("2. Vanilla  Rs 130/-")
print("3. ButterScotch  Rs 75/-")
print("4. MangoDango  Rs 130/-")

while done==0:
    choice = int(input("Enter your Choice ! : "))
    
    if choice==1 or choice==3:
        price = price+75
    elif choice==2 or choice==4:
        price = price+130        
    else:
        print("Something Wrong!")
        
    more = input("Good Choice! Would you like to buy more? ")
    
    if more =="Yes"or more =="yes":
        done = 0
    else:
        done =1
        print("\nThanks for the purchase.\nYour bill is : Rs "+ str(price))