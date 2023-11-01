import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def ask_for_input(self):

        while True:
            guess = input("please guess a letter of the alphabet:")   
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def check_guess(self, guess):

        guess = guess.lower()
        print(guess)
        
        if guess in self.word:
            print(f"Good guess, {guess} is in the word")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letter -= 1
            print(self.word_guessed)
            print("Word Guessed:", ''.join(self.word_guessed))
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not the word. Try again.")
            print(f"you have {self.num_lives} lives left.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break

        elif game.num_letter == 0:
            print("Congratulation! Yo won the game!")
            break

        else:
            game.ask_for_input()

word_list = ["Apples", "Oranges", "Grapes", "Cherries", "Kiwi"]

play_game(word_list)