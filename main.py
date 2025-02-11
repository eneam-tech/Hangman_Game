from random import choice
from random import *
from hangman_pics import HANGMANPICS #pics for the hangman

import sys
import os

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for PyInstaller """
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def Print_Art():
    hangman_art = resource_path("hangman_art.txt")
    with open (hangman_art, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
        print("\n")

#Tries that the player has
lives = 6

def Choose_Word():
    #Randomly choose a word from word list
    words_list = []
    #txt file ref
    hangman_words = resource_path("hangman_words.txt")

    with open(hangman_words, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            words_list.append(line)
            processing_word = choice(words_list)
            chosen_word = str(processing_word).strip()
    
    print(chosen_word)
    return chosen_word
    
#Print _ instead of letters to enable guessing 
def Return_Display(chosen_word):
    display = []
    for letter in chosen_word:
        display += "_"
    print("".join(display))
    return display

def Game_Logic(lives, hangman_pic_index, display, chosen_word):
    
    last_input = None
    while display != chosen_word:
        #Get input from user
        try:
            guess = input("Choose a letter: ").lower().strip()
        except:
            raise ValueError("Insert a letter.")
        print(guess)

        if guess == last_input:
            print(f"You have already chosen {guess}, try another letter!")
        else:
        #check if input letter appears in word
            index = 0
            for letter in chosen_word:
                index += 1
                if guess == letter:
                    display[index-1] = letter
                    print(HANGMANPICS[hangman_pic_index])
        
        #manage wrong letter and -1 lives
            if guess not in chosen_word:
                lives -= 1
                hangman_pic_index += 1
                print(HANGMANPICS[hangman_pic_index])
                print(f"{guess} is not part of the word.\nYou have {lives} lives left")
            print("".join(display))

        last_input = guess

    #win state for the player
        if "".join(display).lower().strip() == chosen_word:
            print("*******************YOU WIN*******************")
            Print_Art()
            print("*******************YOU WIN*******************")
            break

    #loss state for the player
        if lives <= 0:
            print("*******************YOU LOSE*******************")
            Print_Art()
            print("*******************YOU LOSE*******************")
            break

def Main():
    Print_Art()
    hangman_pic_index = 0
    print(HANGMANPICS[hangman_pic_index])
    chosen_word = Choose_Word()
    display = Return_Display(chosen_word)
    Game_Logic(lives, hangman_pic_index, display, chosen_word)

Main()