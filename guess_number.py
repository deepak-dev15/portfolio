import random

print("🎲 Welcome to Deepak's Guess the Number Game!")

# Step 1: Computer picks a random number between 1 and 20
secret_number = random.randint(1, 20)

# Step 2: Give the player 5 chances
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt} - Enter your guess (1-20): "))

    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"😢 Sorry, you ran out of attempts. The number was {secret_number}.")
