import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7

    for attempt in range(1, max_attempts + 1):
        print("Attempt number:", attempt)

        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low!\n")

        elif guess > random_number:
            print("Too high!\n")

        else:
            print("\nYou found the number. Great job!")
            break 

    else:
        print(f"\nToo many guesses. You lose. The number was {random_number}.")


number_guessing_game()
