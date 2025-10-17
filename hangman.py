import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hangman_images =[
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#create a list of randomized words
game_words=["song", "software", "birthday", "student", "medicine", "world", "message", "physics", "apple", "strategy", "chocolate"]

#print welcome
print("Welcome to my Hangman Simulator!")

#start running the program
is_running=True
while is_running:
    #create the correct/chosen word
    chosen_word=random.choice(game_words)
    correct_answer=list(chosen_word)

    correct_letters=[]
    guessed_letters=[]
    
    #create the blank/guessing list
    for i in range(len(correct_answer)):
        correct_letters.append("_")
      
    guess_count=0
    
    #start playing the game
    is_playing=True
    while is_playing:
        #create the image and list
        print(hangman_images[guess_count])
        print(correct_letters)
        print(f"You have guessed: {guessed_letters}")
        
        #start guessing the letters
        is_guessing=True
        while is_guessing:
            guess=input("What letter would you like to guess? ")
        
            #check that the letters guessed has not alreadt been guessed
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                is_guessing=False
            else:
                print("You've already guessed this letter, please enter a new guess.")
        
        #create variable to decide if the guess is correct
        is_correct=False
        for i in range(len(correct_answer)):
            if guess==correct_answer[i]:
                #if the answer is correct set variable true and set the '_' to the letter
                correct_letters[i]=guess
                is_correct=True
            else:
                pass
        
        #if it is false print that it was incorrect    
        if is_correct==False:
            print("Sorry your guess was incorrect\n")
            guess_count+=1
        #if it is true then print it was corrent
        else:
            print("Your guess was correct!\n")
        
        #if they have won then print so
        if correct_letters==correct_answer:
            print("You have won!!")
            print(f"The word was {chosen_word}.")
            is_playing=False
        #if the hangman is created, print they lost
        elif guess_count==6:
            print("Sorry, you have lost :(")
            print(f"The word was {chosen_word}.")
            is_playing=False
        #if neither, pass and continue playing
        else:
            pass
    #ask them if they want to play again           
    choice=input("\nWould you like to play again? ")
    if choice.startswith('y'):
        pass
    else:
    #if they don't, break the game
        is_running=False
        
print("\nThank you for playing!!")
