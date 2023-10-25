import random

word_list = ["Apples", "Oranges", "Grapes", "Cherries", "Kiwi"]

word = random.choice(word_list)

print(word_list)
print(word)

guess = input("Please enter any letter:")
if len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")