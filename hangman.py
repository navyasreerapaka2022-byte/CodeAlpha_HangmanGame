import random

# Predefined words
words = ["apple", "tiger", "school", "python", "flower"]

# Computer selects a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
wrong_attempts = 0

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Main game loop
while wrong_attempts < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts:", wrong_attempts)
    print("Remaining attempts:", max_attempts - wrong_attempts)

    # Check whether the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")