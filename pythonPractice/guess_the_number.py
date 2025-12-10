import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print(f"[DEBUG] The number is: {number_to_guess}")  # 🔍 Show the number temporarily

    attempts = 0
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
