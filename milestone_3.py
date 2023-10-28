import random

word_list = ["Apples", "Oranges", "Grapes", "Cherries", "Kiwi"]

word = random.choice(word_list)

def check_guess(guess):
   
    guess = guess.lowercase()

    if guess in word:
        print("Good guess, {guess} is in the word")
    else:
        print("Sorry, {guess} is not the word. Try again.")
    
def ask_for_input():

    while True:
     
        guess = input("please guess a letter of the alphabet:")    
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid input, please enter a single letter of the Alphabet:")

        check_guess(guess)
    #This is calling the function inside this function to check if the guess is in the word outside the loop

ask_for_input()