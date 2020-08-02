## IMPORTS
from random import choice
import os
import numpy as np
from word_handling import *
import pickle


## VARIABLES (FEEL FREE TO CHANGE THESE)
WORD_LIMIT = 100
WORDS_PER_LINE = 10


## GET THE STORED MARKOV CHAIN
MARKOV = {}
p_in = open('./generated_markov/markov_chain_dict.pickle','rb')
MARKOV = pickle.load(p_in)


# GENERATE SOME LYRICS FROM THE MARKOV CHAIN STARTING FROM A RANDOM WORD
# PRINTING <WORDS_PER_LINE> NUMBER OF WORDS PER LINE
LYRICS=""
WORD_LIMIT-=1
prev = choice(list(MARKOV.keys())) # RANDOM STARTING WORD
while WORD_LIMIT>=0:
    next_word = choice(MARKOV[prev])
    if(WORD_LIMIT%WORDS_PER_LINE==0) : LYRICS+=f"{next_word}\n"
    else : LYRICS+=f"{next_word} "
    prev = next_word
    WORD_LIMIT-=1
print(LYRICS)


'''
# SAVE THE LTRICS
save = input("Do you want to save the generated lyrics? (y/n) : ")
if save == 'y' or save == 'Y':
    filename = input("Enter file name : ")
    with open(f"./generated/{filename}.txt",'w') as save:
        save.write(LYRICS)
        print(f"{filename}.txt saved in ./generated folder")
else :
    print("\nEXITING\nBYE BYE")
'''
