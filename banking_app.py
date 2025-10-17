#define functions

def get_info():
    
    print("Welcome to the Python Banking Application!")
    
    user_name=input("What is your name? ").title()
    savings_deposit=int(input("How much would you like to deposit into your savings account? "))
    checking_deposit=int(input("How much would you like to deposit into your checking account? "))
    
    account={
        "Name":user_name,
        "Savings Account":savings_deposit,
        "Checking Account":checking_deposit,
        }
        
    return account


def make_deposit(bank_account, account_type, amount_deposited):
    if account_type.startswith('S'):
        bank_account["Savings Account"]+=amount_deposited
        print(f"Your account now has {bank_account['Savings Account']} dollars.")
    elif account_type.startswith('C'):
        bank_account["Checking Account"]+=amount_deposited
        print(f"Your account now has {bank_account['Checking Account']} dollars.")
    
def make_withdrawal(bank_account, account_type, amount_withdrawn):
    if account_type.startswith('S'):
        bank_account["Savings Account"]-=amount_withdrawn
        if bank_account["Savings Account"]<0:
            print("Sorry this will result in a negative balance, no changes were made.")
            bank_account["Savings Account"]+=amount_withdrawn
        else:
            pass
    elif account_type.startswith('C'):
        bank_account["Checking Account"]-=amount_withdrawn
        if bank_account["Checking Account"]<0:
            print("Sorry this will result in a negative balance, no changes were made.")
            bank_account["Checking Account"]+=amount_withdrawn
        else:
            pass
    
def display_info(bank_account):
    print("Current Account Information: ")
    
    for k,v in bank_account.items():
        print(f"{k} : {v}")
    
   
#main code

user_account=get_info()

#begin running application
is_running=True
while is_running:
    
    #print user information
    print()
    display_info(user_account)
    
    #gather information retaining to transaction/account type
    account_type=input("\nWhat type of account would you like to access (savings/checking)? ").title()
    transaction_type=input("Would you like to make a deposit or withdrawal? ").lower()
    amount=int(input("How much money would you like to work with? "))
    
    #check to see if it is a saving or checking account
    if account_type=="Savings" or "Checking":
    #run function based on the desired transaction type
        if transaction_type=="deposit":
            make_deposit(user_account, account_type, amount)
        elif transaction_type=="withdrawal":
            make_withdrawal(user_account, account_type, amount)
        else:
            print("That is an invalid option, no changes were made.")
    else:
        print("Sorry, this account can not be accessed.")
        
    #ask if they want to continue running
    continue_running=input("\nWould you like to make another transaction (y/n)? ")
    if continue_running.startswith('n'):
        is_running=False
    else:
        pass

#display final information
print()
display_info(user_account)

#print goodbye
print("\nThank you for choosing Python Banking")
