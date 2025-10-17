import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#print summary
print("-----------POWER BALL SIMULATOR-----------")
print("The power ball is a lottery game where 5 'white' balls and 1 'red' ball are selected at random from a sequence of numbers.")
print("The 'white' balls are chosen from 69 balls numbered 1 through 69.")
print("The 'red' balls are chosen from 26 balls numbered 1 through 26")
print("The 'white' balls are sorted numreically with the 'red' ball appended at the end.")
print("For example, a winning number might be: 7, 28, 33, 48, 60, 13")

#set the numbers
WHITE_NUMBER=69
RED_NUMBER=26

#ask user if they want to change the amount of numbers
choice=input("\nWould you like to change the possible amount of white numbers? ")
if choice.startswith('y'):
    WHITE_NUMBER=int(input("How many white balls do you want to choose from? "))
else:
    print("Okay continuing...")
choice=input("\nWould you like to change the possible amount of red numbers? ")
if choice.startswith('y'):
    RED_NUMBER=int(input("How many red balls do you want to choose from? "))
else:
    print("Okay continuing...")

#create flag variable for the system
is_running=True

while is_running:
    #create the winning numbers
    winning_ticket=[]
    
    #set the white numbers
    while len(winning_ticket)<5:
        white_number=random.randint(1,WHITE_NUMBER)
        if white_number not in winning_ticket:
            winning_ticket.append(white_number)
            
    #sort the list
    winning_ticket.sort()
    
    #set the red number
    red_number=random.randint(1,RED_NUMBER)
    winning_ticket.append(red_number)
    
    #determine the odds/total number of tickets
    total_tickets=int((WHITE_NUMBER*(WHITE_NUMBER-1)*(WHITE_NUMBER-2)*(WHITE_NUMBER-3)*(WHITE_NUMBER-4))*RED_NUMBER//120)
    print(f"\nFor this powerball you have a 1 in {total_tickets} odds of winning with a singular ticket.")
    
    purchased_tickets=[]
    
    #create variable for purchasing tickets
    isnt_digit=True
    
    while isnt_digit:
        tickets=input("\nHow many tickets would you like to purchase? ")
        
        #check if its a digit
        if tickets.isdigit():
            tickets=int(tickets)
            isnt_digit=False
        else:
            print("Your input is invalid, please enter a valid digit.")
    
    #if the amount of tickets purchased is larger than total tickets set equal
    if tickets>total_tickets:
        tickets=total_tickets
    
    #while the purchased tickets length is less than request tickets run this loop
    while tickets!=len(purchased_tickets):
        current_ticket=[]
        
        #dertmine the white and red numbers the same as winning ticket
        while len(current_ticket)<5:
            white_number=random.randint(1,WHITE_NUMBER)
            if white_number not in current_ticket:
                current_ticket.append(white_number)
        
        current_ticket.sort()
    
        red_number=random.randint(1,RED_NUMBER)
        current_ticket.append(red_number)
        
        #check if ticket is in the list
        if current_ticket not in purchased_tickets:
            print(f"Ticket Purchased: {current_ticket}")
            purchased_tickets.append(current_ticket)
        else:
            pass
    
    #print powerbll summary
    print("\n---Welcome to the Power Ball---")
    print(f"\nTonight's winning numbers are:{winning_ticket}")
    
    input("\nPress enter to see if you have a winning ticket!")
    
    #check for winning ticket
    for ticket in purchased_tickets:
        if ticket==winning_ticket:
            winner=True
            break
        else:
            winner=False
    
    #print if the user has won
    if winner==True:
        print("Congratulations! You won the powerball!!!!")
    if winner==False:
        print("Sorry! You're a loser :(")
    
    #ask the user if they want to play again    
    choice=input("\nWould you like to play again?")
    if choice.startswith('y'):
        pass
    else:
        is_running=False
        
print("Thank you for using the powerball simulator!")
