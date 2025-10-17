import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Define the Creature class
class Creature():
    """A Tamagotchi clone"""
    def __init__(self, given_name):
        """Inititalize attributes of the Creature"""
        self.name = given_name
        
        #Attributes to track playing the game (0 - 10)
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        
        self.is_alive = True
        self.is_sleeping = False
        self.food = 2 #Represents the food inventory
    
    
    def eat(self):
        """Simulate eating and lower Creature hunger"""
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print (f"\nYum! {self.name} ate a great meal")
        else:
            print(f"\n{self.name} doesn't have any food! Better Forage for use.")
        
        #if hunger less than zero, set it to 0
        if self.hunger < 0:
            self.hunger = 0
    
    
    def play(self):
        """Play a guessing game"""
        value = random.randint(0, 2)
        print(f"\n{self.name} wants to play a game!")
        print(f"{self.name} is thinking of a number 0, 1 or 2.")
        guess = int(input("What is your guess: "))
        
        #Lower the boredom attrebute based on the users guess
        if guess == value:
            print("THAT IS CORRECT!!!")
            self.boredom -= 3
        else:
            print(f"WRONG! {self.name} was thinking of {value}")
            self.boredom -= 1
            
        #If the boredom is less than zero
        if self.boredom < 0:
            self.boredom = 0
    
    
    def sleep(self):
        """Put the Creature to sleep"""
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 3
        print("\nZzzzzz.....Zzzzzz.....Zzzzzz......")
        
        #If attributes go negative
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0
    
    
    def awake(self):
        """Wake the Creature up"""
        #Creature has a 1/3 change to wake up.
        value = random.randint(0, 2)
        if value == 0:
            print(f"{self.name} just WOKE UP!")
            self.is_sleeping = False
        else:
            print(f"{self.name} won't wake up...")
            self.sleep()
    
    
    def clean(self):
        """Clean the Creature"""
        #Take a bath to COMPLETELY clean the creature
        self.dirtiness = 0
        print(f"{self.name} has taken a bath; ALL CLEAN!")
    
    
    def forage(self):
        """Forage for food for this Creature"""
        #Increase the food syupply randomly between 0 to 4 pieces
        #Print an update message to the player
        #Make the creature a little dirty
        food_found = random.randint(0, 4)
        self.food += food_found
        print(f"{self.name} found {food_found} peices of food!")
        self.dirtiness += 2
    
    
    def show_values(self):
        """Show the current information for this Creature"""
        print(f"\nCreature Name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredom (0-10): {self.boredom}")
        print(f"Tiredness (0-10); {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")
        
        print(f"\nFood Inventory: {self.food} pieces")
        
        #show current sleep status
        if self.is_sleeping:
            print("Creature Status: Is Sleeping")
        else:
            print("Creature Status: Is Awake")
     
    
    def increment_values(self, diff):
        """Increase creature attibutes based on difficulty level"""
        self.hunger += random.randint(0, diff)
        self.dirtiness += random.randint(0, diff)
        
        if self.is_sleeping == False:
            self.boredom += random.randint(0, diff)
            self.tiredness += random.randint(0, diff)

    
    def kill(self):
        """Check to see if kill (or sleep) conditions are met and kill the creature"""
        #first two checks are for kill
        if self.hunger>=10:
            print(f"\n{self.name} has starved to death...")
            self.is_alive=False
        elif self.dirtiness>=10:
            print(f"\n{self.name} has suffered an infection and died...")
            self.is_alive=False
        #next two checks are for sleep
        elif self.boredom>=10:
            self.bordom=10
            print(f"\n{self.name} is bored and going to sleep.")
            self.is_sleeping=True
        elif self.tiredness>=10:
            self.tiredness=10
            print(f"{self.name} is so sleepy and going to sleep.")
            self.is_sleeping=True
        
    

class Game():
    """A helper class to handle all gameplay operations"""
    def __init__(self):
        """Initialize the Game"""
        print("Welcome to the Pythonagachi Simulator App")
        
        #Get the game difficulty level
        self.difficulty = int(input("Please choose a difficulty level (1-5): "))
        if self.difficulty > 5:
            self.difficulty = 5
        elif self.difficulty < 1:
            self.difficulty = 1
            
        #Get user input for creature name and make a Creature.
        creature_name = input("What would you like to name your pet: ").title()
        self.creature = Creature(creature_name)
        
        #Initialize other attributes
        self.round_number = 1
        self.player_move = ""
    
    
    def show_menu(self):
        """Show the game menu to the player.  If Creature is sleeping, the player 
        can only  try to wake the creature up by default"""
        #If  the creature is sleeping, only allow user to wake it up
        #hard code this value for sneaky players
        if self.creature.is_sleeping:
            self.player_move =  input("\nEnter  (6) to try and wake up: ")
            self.player_move = '6'
        #Creature is awake,  give the user full  options
        else:
            print("\nEnter (1) to eat.")
            print("Enter (2) to play.")
            print ("Enter (3) to sleep.")
            print ("Enter (4) to take a bath.")
            print ("Enter (5) to forage for food.")
            
            self.player_move = input("What  is your choice: ")
        
    
    
    def call_action(self):
        """Call the appropriate Creature method based on user input"""
        if self.player_move == "1":
            self.creature.eat()
        elif self.player_move == "2":
            self.creature.play()
        elif self.player_move == "3":
            self.creature.sleep()
        elif self.player_move == "4":
            self.creature.clean()
        elif self.player_move == "5":
            self.creature.forage()
        elif self.player_move == "6":
            self.creature.awake()
        #user entered an invalid input. We arent calling any method
        else:
            print("Sorry,  that is not a valid move.")
    
    
    def update(self):
        """Update the Game: complete one round of gameplay"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Round #{self.round_number} Summary")
        
        #An individual round should do the following:
        #Show all values for the creature, get player's move, call the appropriate Creature method
        self.creature.show_values()
        self.show_menu()
        self.call_action()
        
        #Summarize the effects of the current round
        self.creature.show_values()
        input("\nPress (enter) to continue...")
        
        #Increment other attributes
        self.creature.increment_values(self.difficulty)
        
        #Check for death
        self.creature.kill()
        
        #Round is over, incriment the round number
        self.round_number+=1
        

    def game_over(self):
        """End the game and summerize the results"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("R.I.P")
        self.creature.show_values()
        print(f"{self.creature.name} survived a total of {self.round_number-1} rounds.")
        
    
#The main code
is_running = True
while is_running:
    #Create a game object
    my_game = Game()
    
    #Game and Creature are initialized.
    #Run the main gameplay loop.
    while my_game.creature.is_alive:
        my_game.update()
        
    #the creature died, game over
    my_game.game_over()
    
    #ask to play again
    choice=input("\nWould you like to play again (y/n): ").lower()
    if choice!="y":
        is_running=False
    
print("\nThank you for playing this game!")
