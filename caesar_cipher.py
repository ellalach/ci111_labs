LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ "

#define each flag variable for the loops
is_running=True
is_valid=False
is_message=False
is_digit=False

#begin running the whole ciper system
while is_running:
    #ask what mode user would like to operate in
    user_input=input("What mode would you like to operate in: \n(e) Encrypt \n(d) Decrypt\n").lower()
    if user_input=='e' or user_input=='d':
        is_valid=True
    #if not valid ask them to restart
    else:
        print("\nSorry your choice is invalid, please try again.")
        
    #once valid begin running next loop
    while is_valid:
        
        #ask for the next message
        message=input("\nWhat message would you like to use? ")
        
        if message=="":
            print("\nSorry your message was not recieved, please try again. ")
        else:
            is_message=True
            message=message.upper()
            
        #once valid start running next loop
        while is_message:
            
            #ask for the shift key
            shift_key=input("\nWhat shift key would you like to use? ")
            
            #check for digit
            if shift_key.isdigit():
                shift_key=int(shift_key)
                is_digit=True
            else:
                print("\nYour input could not be interpreted as a digit, please try again.")
                
            #once digit run next loop
            while is_digit:
                
                ciper_message=""
               
               #start creating letters into index
                for letter in message:
                 
                    if letter in LETTERS:
                       
                       letter_index=LETTERS.find(letter)
                       
                    #once index is found determine the mode
                    if user_input=='e':
                        new_letter_index=(letter_index+shift_key)%27
                        new_letter=LETTERS[new_letter_index]
                        ciper_message+=new_letter
                            
                    elif user_input=='d':
                        new_letter_index=(letter_index-shift_key)%27
                        new_letter=LETTERS[new_letter_index]
                        ciper_message+=new_letter
                        
                    else:
                        print("\nSorry, there was an error")
                        break
                #print the new message
                input("\nPress enter to see your new message:")
                print(f"Your new message is: {ciper_message}")
                
                #ask if they want to run it again
                choice=input("\nWould you like to run this program again? ")
                
                #if no break all the loops
                if choice.startswith('n'):
                    is_digit=False
                    is_message=False
                    is_valid=False
                    is_running=False
                #if yes just break every loop but the overall program
                else:
                    is_digit=False
                    is_message=False
                    is_valid=False
#print ogodbye                    
print("\nThank you for using my program!")
