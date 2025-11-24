import random

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game():
    print("===== NUMBER GUESSING GAME =====")
    print("I am thinking of a number between 1 and 100...")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_int("Enter your guess: ")
        attempts += 1

        if guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
