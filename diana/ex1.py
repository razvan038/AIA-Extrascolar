import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    num_guesses = 0
    
    while True:
        # Get user's guess
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function to start the game
guess_number()