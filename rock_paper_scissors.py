import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#print welcome
print("Welcome to the Rock Paper Scissors simulator!")

#gather user inputs
games=int(input("How many games would you like to play? "))

moves=["rock", "paper", "scissors"]
player_score=0
computer_score=0

#begin the game simulation
for i in range(games):
    #print round summary
    print(f"\nThis is round {i+1}")

    print(f"Computer Score: {computer_score}")
    print(f"Player Score: {player_score}")
    
    #gather computer and user moves
    computer_choice=random.choice(moves)
    player_choice=input("\nWhat move would you like to play? ").lower()
    print(f"\tComputer's Choice: {computer_choice}")
    print(f"\tPlayer's Choice: {player_choice}")
    
    #print results if player choice is rock
    if player_choice=="rock":
        if computer_choice=="rock":
            print("\tIts a tie!")
        elif computer_choice=="paper":
            print("\tPaper covers rock!!")
            print("\tComputer wins!")
            computer_score+=1
        else:
            print("\tRock crushes scissors!!")
            print("\tPlayer wins!")
            player_score+=1
           
    #print results if player choice is paper 
    elif player_choice=="paper":
        if computer_choice=="paper":
            print("\tIts a tie!")
        elif computer_choice=="scissors":
            print("\tScissors cuts paper!!")
            print("\tComputer wins!")
            computer_score+=1
        else:
            print("\tPaper covers rock!!")
            print("\tPlayer wins!")
            player_score+=1
    
    #print results if player choice is scissors
    elif player_choice=="scissors":
        if computer_choice=="scissors":
            print("\tIts a tie!")
        elif computer_choice=="rock":
            print("\tRock smashes scissors!!")
            print("\tComputer wins!")
            computer_score+=1
        else:
            print("\tScissors cut paper!!")
            print("\tPlayer wins!")
            player_score+=1
    
    #print results for an invalid input
    else:
        print("\tThats not a valid option.")
        print("\tComputer Wins!")
        computer_score+=1
        
#print final game summary
print("\nFinal game summary...")
print(f"\tRounds Played: {games}")
print(f"\tComputer Score: {computer_score}")
print(f"\tPlayer Score: {player_score}")

#print winner
if computer_score>player_score:
    print("\tWinner: Computer!!")
elif player_score>computer_score:
    print("\tWinner: Player :(")
else:
    print("\tIt was a tie!")
