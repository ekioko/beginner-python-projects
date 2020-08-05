#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:27:15 2020

@author: emmakioko
"""


import pandas as pd
from random import randint
# import tkinter as tk


df = pd.read_csv("quote_game.csv")
df_bios = pd.read_csv("quote_game_authors.csv")
new_df = pd.concat([df, df_bios], axis=1)

def choose_quote():
    next_row = randint(1,108)
    return next_row

def start_game(row=1):
    quote = new_df["Quote"][row].lower()
    author = new_df["Author"][row].lower()
    print(quote) 
   
    remaining_guesses = 4
    user_guess = ''
    
    while user_guess.lower() != author and remaining_guesses > 0:
        user_guess = input(f"who said this? Guesses remaining: {remaining_guesses} \n").lower()
        
        if user_guess == author:
            print("Congrats! You won.")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            hint_1 = new_df["Biographical Info"][row]
            print(f"ok, I'll give you a hint {hint_1}")
        
        elif remaining_guesses == 2:
            hint_2 = new_df["First Initial"][row]
            print(f"ok, I'll give you another hint, their first name starts with the letter: {hint_2}")
        
        elif remaining_guesses == 1:
            hint_3 = new_df["Last Initial"][row]
            print(f"ok, I'll give you one last hint, their last name starts with the letter: {hint_3}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {author}.")
            break

    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("would you like to play again? (y/n) ").lower()
    if again in ('yes', 'y'):
        return start_game()
    else:
        print("OK, GOODBYE!")

        
game = choose_quote()
start_game(game)
    
# while guess <= 4:retu
#     if i != author:
#         print("Sorry,")
        
# window.mainloop()

# # initialize GUI
# window = tk.Tk()
# window.title("Can you guess the quote?")

# lblInst = tk.Label(window, text=chosen_row)
# e = tk.Entry(window)
# e.pack()

# e.focus_set()

# def callback():
#     return e.get()



# # add elements to grid
# #lblInst.grid(row=0,column=0,columnspan=5)

# print(chosen_row)
# print(author)