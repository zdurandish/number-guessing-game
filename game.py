import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randint(0, 100)

repeat = 0
if difficulty == "hard":
    repeat += 5
else:
    repeat += 10

game_over = False

while not game_over and repeat > 0:
    print(f"You have {repeat} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    if not user_guess == random_number:
        repeat -= 1
        if user_guess > random_number:
            print("Too high!")
        else:
            print("Too low!")
        if repeat > 0:
            print("Guess again!")
    else:
        game_over = True
        print(f"You got it! The random number was {random_number}. You win")

if repeat == 0:
    print("You ran out of guesses, you lost!")