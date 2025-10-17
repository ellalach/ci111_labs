print("Welcome to the Factor Generator!")

#create flags to control loops
is_running=True
is_number=False
       
#begin running first loop
while is_running:
    #ask for number
    number=input("\nWhat number would you like to determine a factor for? ")
    #confirm if it is a number
    if not number.isdigit():
        print("Sorry your input cannot be interpreted as an integer.")
        print("Please try again.")
    else:
        #once it is confirmed it is a number, begin second loop
        number=int(number)
        is_number=True
        
    while is_number:
        factors=[]
        
        #start determining factors
        for i in range(1,number+1):
            if number%i==0:
                factors.append(i)
            else:
                pass
        
        #if number is not a perfect square root, print with this loop
        if (int(len(factors)))%2==0:
            print(f"\nThe following factors of {number} are:")
            for i in range(int((len(factors))/2)):
                print(f"\t{factors[0+i]}*{factors[-1-i]}")
        
        #if number is perfect square root, print using this loop
        else:
            #the difference is that it adds one to the range to account for odd number of factors
            for i in range(int((len(factors))/2)+1):
                print(f"\t{factors[0+i]}*{factors[-1-i]}")           
        
        #ask the user if they want to continue
        user_continue=input("\nWould you like to run this program again (y/n)? ")
        if user_continue.startswith('n'):
            #break both loops to exit
            is_number=False
            is_running=False
        else:
            #break only the factoring loop to determine next number
            is_number=False

print("\nThank you for using my program!")
