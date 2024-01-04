"""
Create a Python file named Midterm-Q2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

"""

import random

def choose_word():
    words = ["prep", "Mr O", "fairfield", "xavier", "berchman", "ignatious", "arrupe", "computer", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 9
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    attempts = 0
    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! {max_attempts - attempts} attempts left.")
        else:
            print("Correct guess!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if current_display == word_to_guess:
            print("Congratulations! You guessed the word.")
            break

    if current_display != word_to_guess:
        print(f"Sorry, you're out of attempts. The word was {word_to_guess}.")

if __name__ == "__main__":
    hangman()
