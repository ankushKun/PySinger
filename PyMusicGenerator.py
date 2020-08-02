import random
from replacement import *

Markov = {}

word_list = get_words_list_from_file('./data/pkmn.txt')

for word in word_list[:-1]:
    print(word)
