import random

def main():
    random_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        guess = input("Enter your guess: ")

        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1  

        
        if guess < random_number:
            print("Your guess is too low. Try again!")
        elif guess > random_number:
            print("Your guess is too high. Try again!")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {random_number} correctly in {attempts} attempts.")

if __name__ == "__main__":
    main()