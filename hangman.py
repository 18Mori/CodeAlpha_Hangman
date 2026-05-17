import random

words = ["python", "software", "logic", "coding", "script"]
word = random.choice(words)
# setup variables
guessed_letters = []

def show_word():
    show = ""
    for letter in word:
        if letter in guessed_letters:
            show += letter + " "
        else:
            show += "_ "
    return show.strip()
print("Welcome to Hangman!")
print("Try to guess the word, one letter at a time.")

while True:
    print(f"\nWord: {show_word()}")

    guess = input("Guess a letter: ").lower()

    # add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print(f"Nice! '{guess}' is in the word.")

    # Check for a win
    if "_" not in show_word():
        print(f"\nCongrats! You guessed the word: {word}")
        break