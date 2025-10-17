#define functions
def get_loan_info():
    
    int_principal=float(input("Enter the loan amount: "))
    interest_rate=float(input("Enter the interest rate: "))
    payment=float(input("Enter the desired monthly payment amount: "))
    
    loan={
        "initial principal":int_principal,
        "current principal":int_principal,
        "rate":interest_rate,
        "monthly payment":payment,
        "months paid":0,
        "money paid":0,
        }
        
    return loan
    

def show_loan_info(current_loan):
    print("---Current Loan Information---")
    
    for k,v in current_loan.items():
        print(f"{k.title()} : {v}")
        

def collect_interest(current_loan):
    current_loan["current principal"]+=current_loan["current principal"]*(current_loan["rate"]/12)
    current_loan["current principal"]=round(current_loan["current principal"], 2)


def make_monthly_payment(current_loan):
    current_loan["months paid"]+=1
    
    if current_loan["current principal"]-current_loan["monthly payment"]>0:
        current_loan["current principal"]-=current_loan["monthly payment"]
        current_loan["money paid"]+=current_loan["monthly payment"]
    
    else:
        excess_payment=current_loan["monthly payment"]-current_loan["current principal"]
        current_loan["money paid"]+=excess_payment
        current_loan["current principal"]=0
        
    round(current_loan["current principal"], 2)
    

def summarize_loan(current_loan):
    print("\nCongratulations!!!!!!! You paid off your loan!")
    print(f"It took you {current_loan['months paid']} months.")
    print(f"Your inital loan was {current_loan['initial principal']} at a rate of {current_loan['rate']}.")
    print(f"Your monthly payment was {current_loan['monthly payment']}.")
    print(f"You spend {current_loan['money paid']} dollars paying off your loan.")
    print(f"This means you spent {(current_loan['money paid'])-(current_loan['initial principal'])} dollars on interest!")
    

#main code
print("Welcome to the Python Loan Calculator!")

user_loan=get_loan_info()
show_loan_info(user_loan)

#begin loop
while user_loan['current principal']>0:
    
    print()
    input("---Press enter to pay for your loan---")
    
    #determine if interest will outpace the user
    if user_loan['current principal']>user_loan['initial principal']:
        print("\nYou will never pay off your loan, you cannot escape interest :(")
        break
    else:
        collect_interest(user_loan)
        make_monthly_payment(user_loan)
        show_loan_info(user_loan)

#if they pay off the loan print the summary    
if user_loan['current principal']==0:
    summarize_loan(user_loan)

#if they cannot pay off their loan inform them
else:
    print("\nSorry, you can not pay off your loan...")
