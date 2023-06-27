# Hangman
#   +---+
#   O   |
#  /|\  |
#  / \  |
#      ===
import time
import random
import hangman_data as DATA

wordindex = random.randint(0, len(DATA.words) - 1)
word = DATA.words[wordindex]

max_turns = len(DATA.pics)
turn = 1

guessed_letters = []

complete = False

print(word)

print("Je hebt " + str(max_turns) +
      " beurten, geef telkens 1 karakter en druk enter; wat is het woord ...")

while ((turn < max_turns + 1) and not complete ):
    # we willen laten zien welke beurt nu is en die begint bij 1 dus
    letter = input("beurt " + str(turn) + " wat is je letter: ")

    # voor iedere letter willen we weten of die voorkomt en op welke posistie
    if (letter in word):
        guessed_letters.append(letter)
    else:
        print(DATA.pics[turn - 1])
        turn = turn + 1

    print("  ", end='')
    complete = True
    for letter_in_word in word:
        if(letter_in_word in guessed_letters):
            print(letter_in_word, end='')
        else:
            complete = False
            print(".", end='')
    print("\n")

if(complete):
    print("\nGefeliciteerd je hebt het woord geraden")    
else:
    print("\nJe bent DOOD, jammer")

