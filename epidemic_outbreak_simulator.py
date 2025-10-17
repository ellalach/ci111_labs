import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Person():
    """create a person blueprint"""
    def __init__(self):
        self.is_infected=False
        self.is_dead=False
        self.days_infected=0
        
    def infect(self, infection_probabilty):
        """determine if the person becomes infected"""
        chance=random.randint(0,100)
        if chance<infection_probabilty:
            self.is_infected=True
    
    def heal(self):
        """heal an infected"""
        self.is_infected=False
        self.days_infected=0
    
    
    def die(self):
        """person dies of infection"""
        self.is_dead=True
        self.is_infected=False
        
        
    def update(self, mortality_rate, infection_duration):
        """update a person"""
        if self.is_infected==True:
            self.days_infected+=1
            if (random.randint(0,100))<mortality_rate:
                self.die()
            elif self.days_infected==infection_duration:
                self.heal()
            
    
class Population():
    """create a class for the total population"""
    def __init__(self):
        """create the population"""
        
        self.population_size=int(input("What is the current size of the population? "))
        
        self.infection_percent=float(input("What percent of the population is currently infected? "))/100
        self.infection_probablity=float(input("What is the probability that someone will get infected when in they come in contact with the disease? "))
        self.infection_duration=float(input("How many days does the infection last? "))
        self.mortality_rate=float(input("What is the mortality rate? "))
        
        self.days_to_sim=int(input("How many days should the simulation last for? "))

        self.current_day_number=1
        self.population_list=[]
        
        for i in range(self.population_size):
            person=Person()
            self.population_list.append(person)
            
    def show_starting_conditions(self):
        """show the inital conditions"""
        print(f"Inital Population Size: {self.population_size}")
        print(f"Inital Percentage of Population Infected: {self.infection_percent*100} %")
        print(f"Infection Duration: {self.infection_duration}")
        print(f"Mortality Rate: {self.mortality_rate} %")
        
        
    def initial_infection(self):
        """determine the infected count"""
        self.infected_count=int(self.population_size*self.infection_percent)
            
        for i in range(self.infected_count):
            self.population_list[i].is_infected=True
            self.population_list[i].days_infected=1
            
        random.shuffle(self.population_list)
        
        self.show_starting_conditions()
        self.display_statistics()
        self.display_graphics()
            
        input("\nPress Enter to Continue: ")
        
    def update(self):
        """update the game day"""
        self.spread_infection()
        self.advance_day()
        self.display_statistics()
        self.display_graphics()
    
    
    def spread_infection(self):
        """spread the infection"""
        for i in range(len(self.population_list)):
            if self.population_list[i].is_dead==False:
                if i==0:
                    if self.population_list[i+1].is_infected==True:
                        self.population_list[i].infect(self.infection_probablity)
                elif i<(len(self.population_list)-1):
                    if self.population_list[i-1].is_infected==True or self.population_list[i+1].is_infected==True:
                        self.population_list[i].infect(self.infection_probablity)
                elif i==(len(self.population_list)-1):
                    if self.population_list[i-1].is_infected==True:
                        self.population_list[i].infect(self.infection_probablity)
                    
    
    def advance_day(self):
        """advace the day"""
        self.current_day_number+=1
        for i in range(len(self.population_list)):
            self.population_list[i].update(self.mortality_rate, self.infection_duration)
    
    
    def display_statistics(self):
        """display the stats of the current round"""
     
        self.total_infected_count=0
        self.total_death_count=0
        
        for i in range(len(self.population_list)):
            if self.population_list[i].is_infected==True:
                self.total_infected_count+=1
            elif self.population_list[i].is_dead==True:
                self.total_death_count+=1
        
        self.infected_percent=round((self.total_infected_count/self.population_size)*100,4)
        self.death_percent=round((self.total_death_count/self.population_size)*100,4)
        
        print(f"\nDay {self.current_day_number}:")
        print(f"{self.infected_percent} percent of the population is infected.")
        print(f"{self.death_percent} percent of the population is dead.")
        print(f"{self.total_infected_count} people are infected.")
        print(f"{self.total_death_count} people are dead.")
    
    def display_graphics(self):
        """print out a visual representation of the infected, dead, etc."""
        status=[]
        
        for i in range(len(self.population_list)):
            if self.population_list[i].is_dead==True:
                character="X"
            else:
                if self.population_list[i].is_infected==True:
                    character="I"
                else:
                    character="O"
            
            status.append(character)
            
        for i in range(len(status)):
            print(status[i], end="-")
        
    
    
#the main code
current_population=Population()
current_population.initial_infection()

is_simulating=True

while is_simulating:
    current_population.update()
    if current_population.current_day_number<current_population.days_to_sim:
        input("\n-Press enter to continue-")
    else:
        is_simulating=False
        
print("\nThe simulation has ended.")
print("-------Summary-------")
current_population.show_starting_conditions()
current_population.display_statistics()
current_population.display_graphics()
