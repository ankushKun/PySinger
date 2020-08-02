## IMPORTS
import numpy as np
import os
from word_handling import *
import pickle

## MARKOV CHAIN
## { 'WORD' : ['next','possible','words','in','array'] }
MARKOV = {}

print('> GETTING WORDS INTO AN ARRAY')
word_arr = np.array([])
# GET THE WORDS FROM TEXT FILES IN ./data FOLDER INTO AN ARRAY
for root,dirs,files in os.walk('./data/'):
    for f in files:
        if os.path.join(root,f).endswith('.txt'):
            word_arr = np.append(word_arr,get_words_from_file(os.path.join(root,f)))
print('> DONE')            

print('> GENERATING MARKOV CHAIN')
# GENERATE THE MARKOV CHAIN USING DICT AND ARRAYS
# FROM THE WORDS OBTAINED FROM THE TEXT FILES
for i in range(len(word_arr)-1):
    prev,nxt=word_arr[i], word_arr[i+1]
    if prev in MARKOV:
        MARKOV[prev] = np.append(MARKOV[prev],[nxt])
    else:
        MARKOV[prev] = np.array([nxt])
print('> MARKOV CHAIN GENERATED')

# SAVE THE MARKOV CHAIN
p_out = open('./generated_markov/markov_chain_dict.pickle','wb')
pickle.dump(MARKOV,p_out)
p_out.close()

'''
print('> STORING MARKOV CHAIN IN ./generated_markov')
os.mkdir('./generated_markov')
with open('./generated_markov/markov_chain_dict.txt','w') as m:
    m.write(str(MARKOV))
'''
print('> MARKOV CHAIN STORED AS ./generated_markov/markov_chain_dict.txt')
