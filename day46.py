from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVER_TURNS = 5

def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return  HARD_LEVER_TURNS


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

answer = randint(1, 100)

guess = int(input("Make a guess:"))
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number")




def my_function():
    for i in range(1, 20):
        if i == 20:
            print("yo")
my_function()






