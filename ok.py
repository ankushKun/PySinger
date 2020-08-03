import os
import numpy as np
from word_handling import get_words_from_file

#word_arr=np.array([])
word_arr=[""]

for root,dirs,files in os.walk('./data/'):
    for f in files:
        word_arr.append(get_words_from_file(os.path.join(root,f)))

with open('hoi1.txt', 'w') as hoi:
    hoi.write(str(word_arr))