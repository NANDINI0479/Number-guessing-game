from random import randint
# from design_logo import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function which check user's answer against original answer

def check_ans(guess, answer, attempts):
    """check answer against guess. Returns the number of attempts remaining"""
    if guess > answer:
        print("Your guess is too high.")
        return attempts - 1
    elif guess < answer:
        print("Your guess is too low.")
        return attempts - 1
    else:
        print(f"You've got the correct answer !!!. It was {answer}.")
        
#Function to decide difficulty level for this game
        
def set_level():
    level = input("Choose a difficulty level. For this, type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def game_start():
    
    #choosing a random number between 1 and 100.
    # print(logo)
    print("Welcome to the Number Guessing Game !!")
    print("According to game, the number is between 1 and 100")
    answer = randint(1, 100)
    print(f"The right answer is {answer}")
    
    attempts = set_level()
    #Repeat the guessing part if the user get it wrong
    
    guess = 0
    while guess != answer:
        print(f"You have {attempts} turns remaining to guess the number")
        
        #Ask the number from user
        guess = int(input("Make any guess:"))
        
        #Show the number of attempts and reduce by 1 if the user guess it wrong
        
        attempts = check_ans(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses. !!! So, You lose :(")
            return 
        elif guess != answer:
            print("Guess Again")
        

game_start()
