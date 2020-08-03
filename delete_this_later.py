import numpy as np
import os
from word_handling import *

words = ""
# GET THE WORDS FROM TEXT FILES IN ./data FOLDER INTO AN ARRAY
for root,dirs,files in os.walk('./data/'):
    for f in files:
        if os.path.join(root,f).endswith('.txt'):
            #print(f)
            words += read_lyrics_from_file(os.path.join(root,f))
            
with open('./words.txt','w') as f:
    f.write(words)
