import random
import os
import numpy as np
from word_handling import *

## MARKOV CHAIN
## { 'WORD' : ['next','possible','words','in','array'] }
MARKOV = {}



## VARIABLES (FEEL FREE TO CHANGE THESE)
WORD_LIMIT = 100
WORDS_PER_LINE = 10



word_arr = np.array([])
# GET THE WORDS FROM TEXT FILES IN ./data FOLDER INTO AN ARRAY
for file_ in os.listdir('./data'):
    word_arr = np.append(word_arr,get_words_from_file(f'./data/{file_}'))



# GENERATE THE MARKOV CHAIN USING DICT AND ARRAYS
# FROM THE WORDS OBTAINED FROM THE TEXT FILES
for i in range(len(word_arr)-1):
    prev,nxt=word_arr[i], word_arr[i+1]
    if prev in MARKOV:
        MARKOV[prev] = np.append(MARKOV[prev],[nxt])
    else:
        MARKOV[prev] = np.array([nxt])



# GENERATE SOME LYRICS FROM THE MARKOV CHAIN STARTING FROM A RANDOM WORD
# PRINTING <WORDS_PER_LINE> NUMBER OF WORDS PER LINE
LYRICS=""
WORD_LIMIT-=1
prev = random.choice(list(MARKOV.keys())) # RANDOM STARTING WORD
while WORD_LIMIT>=0:
    next_word = random.choice(MARKOV[prev])
    if(WORD_LIMIT%WORDS_PER_LINE==0) : LYRICS+=f"{next_word}\n"
    else : LYRICS+=f"{next_word} "
    prev = next_word
    WORD_LIMIT-=1
print(LYRICS)



# SAVE THE LTRICS
save = input("Do you want to save the generated lyrics? (y/n) : ")
if save == 'y' or save == 'Y':
    filename = input("Enter file name : ")
    with open(f"./generated/{filename}.txt",'w') as save:
        save.write(LYRICS)
        print(f"{filename}.txt saved in ./generated folder")
else :
    print("\nEXITING\nBYE BYE")
