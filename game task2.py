import random

def hangman():
    words = ["python", "coding", "intern", "game", "alpha"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print("Word:", display)
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won! The word was:", word)
            break
    else:
       print("Game Over! The word was:", word)
hangman()