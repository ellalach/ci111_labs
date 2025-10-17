print("Welcome to the Prime Number Finder")

is_running=True
while is_running:
    print("\nYou may choose the following:")
    print("\t(a) Determine if a given number is prime.")
    print("\t(b) Determine all prime numbers up to a given value.")
    
    choice=input("\nWhat menu option would you like: ").lower()
    while not choice:
        print("Option not recieved, try again.")
        choice = input("\nWhat menu option would you like: ").lower()

    number=input("\nWhat number would you like to work with: ")
    while not number.isdigit():
        print("That cannot be interpreted as an integer, try again.")
        number=input("\nWhat number would you like to work with: ")
    number=int(number)
    
    if choice == "a":
        is_prime=True
        for i in range(2, number):
            if number%i==0:
                is_prime=False
                break
        
        if is_prime:
            print(f"{number} is prime!")
        else:
            print(f"{number} is not prime.")
            
    elif choice=="b":
        
        primes=[]
        
        for i in range(2,number):
            is_prime=True
            for k in range(2, i):
                if i%k==0:
                    is_prime=False
                    break
                else:
                    pass
            if is_prime==True:
                primes.append(i)
            
        if len(primes)==0:
            print("Sorry your choice does not have any prime numbers.")
        else:
            print(f"\nOkay! Here are all prime numbers from 2 to {number}:")
            print(primes)
    else:
        print("Sorry, that is not a valid menu option.")
        
    choice=input("\nWould you like to run the program again (y/n)? ").lower()
    if choice!="y":
        is_running=False
        
print("\nThank you for using my program.")
