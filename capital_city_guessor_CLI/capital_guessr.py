'''@author Tadiwa Chigwikwi
    24/11/2025
    Simple capital city guessing game, or a user can learn the capitals of specific countries by 
    prompting the program with the country name.'''


import random
from database import countries





#generates 20 random countries and asks user to type in capitals. Calculates score at the end
def play(rounds):
    correct = 0 #keeps track of how many question guessed right

    countries_only = list(countries.keys())
    countries_picked = []
    
    i = 0
    while i <= rounds:
        #generate random country
        country = random.choice(countries_only)
        #want to avoid repetition
        if country not in countries_picked:
            countries_picked.append(country)
            guess = input(f"{country}:  ")
            if guess == "Q" or "q": break
            #if correct
            if check(country, guess):
                print("Correct")
                correct += 1
            #if wrong    
            else:
                print(f"INCORRECT.  The capital of {country} is {countries[country]}.") 
            i += 1       

        else: 
            i -= 1
            continue

    win_percentage = (correct/rounds) * 100
    print(f"You got {correct}/{rounds} capitals correct.  Your win percentage is {win_percentage}")       
        



#checks to see if a capital guessed corresponds to it's country
def check(country, capital):
    if countries[country] == capital:
        return True
    else: return False  


#user prompts a country and system returns its capital
def learn():
    countries_only = list(countries)
    while True:
        country = input("Please enter country or Q to go back to main menu: ")
        if country == "Q":
            break
        if country in countries_only:
            print(countries[country]) #return the capital
        else:
            print("Please enter a UN-recognized country.\n") 


        

         

def main():
    print("Welcome to the geoPro guessing game. Select your choice:\n")
    while True:
        try:
            choice = int(input("1. Play game.\n2. Learn\n0. QUIT\n"))
            if choice == 1:
                #ask how many countries the user wants to guess
                try:
                    rounds_to_play = int(input("How many rounds do you want to play\n"))
                    play(rounds_to_play)
                except ValueError:
                    print("Only integers accepted.")
                    continue    
                
            elif choice == 2:
                learn()
            elif choice == 0:
                print("Nice playing with you, till next time:)")
                break 
        except ValueError:
            print("Please enter a valid integer option from 0 to 2 (inclusive).")           

if __name__ == "__main__":
    main()