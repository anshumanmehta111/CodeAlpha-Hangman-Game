import random

def run_game():
    words = ["python", "coding", "pixel", "laptop", "search"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\n--- New Game Started! ---")

    while incorrect_guesses < max_attempts:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")
        print(f"Attempts left: {max_attempts - incorrect_guesses}")
        
        if "_" not in display_word:
            print("✨ Congratulations! You won! ✨")
            return # Exit the function to go back to the main menu

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(">> Please type a single letter.")
            continue
        if guess in guessed_letters:
            print(f">> Already tried '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f">> Yes! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f">> No, '{guess}' is not there.")

    print(f"\nGame Over! The word was: {secret_word}")

# --- MAIN LOOP ---
while True:
    run_game()
    
    # Ask the player if they want another round
    choice = input("\nWould you like to play again? (yes/no): ").lower()
    if choice not in ["yes", "y"]:
        print("Thanks for playing! Goodbye.")
        break # This breaks the 'True' loop and ends the program
