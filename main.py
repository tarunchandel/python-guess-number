from art import logo
from art import welcome
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

#print the logo and welcome message
def welcome_screen():
  print(logo)
  print(welcome)

#Generate a random number between 1-100
def generate_number(num):
  print(f"I'm thinking of a number between 1 and {num}.")
  result = randint(1,num)
  #print(result)
  return result

#Take level as input from the user. Easy or Hard.
def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return(EASY_ATTEMPTS)
  else:
    return(HARD_ATTEMPTS)

#Condition to check if guess lower or higher than the number
def check(guess, number):
  if guess == number:
    print(f"You got it! The number is {number}.")
    return True
  elif guess < number:
    print ("Too low.")
  else:
    print("Too high.")
  return False

#Made a separate function game
def game():
  welcome_screen()
  number = generate_number(100)
  attempts = set_level()

  #run the loop for 5 or 10 times or till the user inputs the correct answer
  guessed_flag = False
  while attempts > 0 and not guessed_flag:
    
    #print how many attempts are left
    print (f"You have {attempts} attempts remaining to guess the number.")
    attempts -= 1
    
    #ask user for the guess
    guess = int(input("Make a guess: "))
    guessed_flag = check (guess, number)

    #check if attempts are remaining and print the message
    if guessed_flag == False:
      if attempts > 0:
        print("Guess Again.")
      else:
        print("You've run out of guesses, you lose.")
  
#this can be called recursively 
game()
  
    