import random

def guess_the_name():
    names = ["Boisakhi", "Nazia", "Sultana", "Fatema", "Nadia"]
    secret_name = random.choice(names)

    print("🎉 Welcome to the Name Guessing Game! 🎉")
    print("You have 5 attempts to guess the secret name from the following list:")
    print(names)

    attempts = 5

    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Enter your guess: ").strip()
        
        if guess.lower() == secret_name.lower():
            print("🎉 Congratulations! You guessed the right name! 🎉")
            break
        else:
            attempts -= 1
            print("❌ Wrong guess! Try again!")

    if attempts == 0:
        print(f"😢 Sorry, you've used all your attempts! The secret name was: {secret_name}")

if __name__ == "__main__":
    guess_the_name()
