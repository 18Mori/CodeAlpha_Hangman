import random

words = ["python", "software", "logic", "coding", "script"]
word = random.choice(words)
# setup variables
guessed_letters = []
attempts_left = 6
print("--- Hangman Game ---")
print("Try to guess the word, one letter at a time.")

def show_word():
    show = ""
    for letter in word:
        if letter in guessed_letters:
            show += letter + " "
        else:
            show += "_ "
    return show.strip()

while attempts_left > 0:
    print(f"\nWord: {show_word()}")
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Guess a letter: \n").lower()
    # input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    # add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is correct/incorrect
    if guess in word:
        print(f"Nice! '{guess}' is in the word.")
    else:
        attempts_left -= 1
        print(f"Sorry, '{guess}' is not in the word.")

    if "_" not in show_word():
        print(f"\nCongrats! You guessed the word: {word}")
        break
else:
    print(f"\nGame over! You've run out of attempts. The word was: {word}")
    
if __name__ == "__main__":
    show_word()