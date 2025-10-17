print("Welcome to the Database Administrator Program!")

#create dictonary
log_on_information={
    'admin00':'hKVhshS5',
    'admin01':'3Z9sEwWW',
    'admin02':'ptFyjJZP',
    'admin03':'9YBXXdLT' ,
    'admin04':'rjAJewyq',
    }

#ask username
username=input("Enter you username: ")

#begin looping
if username in log_on_information.keys():
    password=input("What is your pasword: ")
    #check for password
    if password==log_on_information[username]:
        print(f"Welcome {username}!")
        #print for admin00
        if username=='admin00':
            print("Here is the current user database:")
            for key, value in log_on_information.items():
                print(f"Username: {key}\tPassword: {value}")
        #begin password changing
        else:
            change_pass=input("Would you like to change your password (yes/no): ")
            if change_pass=="yes":
                new_pass=input("What would you like your new password to be, it must be at least 8 characters long. ")
                #create new password
                if len(new_pass)>=8:
                    log_on_information.update({username:new_pass})
                    print("Okay success! Your password is now updated.")
                else:
                    print("Sorry, your password is not long enough")
                #print current password
                print(f"Your current password is {log_on_information[username]}.")
            #print goodbyes or errors
            else:
                print("Okay, goodbye!")
    else:
        print("Sorry, your password is incorrect.")
else:
    print("Sorry, your username is not in our database.")
