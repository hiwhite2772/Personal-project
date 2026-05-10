import random

# Generate a random number between 1 and 100
secret = random.randint(1, 100)

print("=== Guess the Number Game ===")
print("I have chosen a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it 🎉")
        break
