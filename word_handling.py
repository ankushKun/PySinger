import numpy as np

# VARIABLES
puntuations = ['.',',','"',"'",'!','*',';','-','(',')']

# FUNCTION TO REMOVE ALL PUNTUATION FROM A TEXT FILE
def replace(file_location):
    try:
        with open(file_location,"r") as lyrics:
            new_lyrics=""
            for line in lyrics:
                new_line=line
                for puntuation in puntuations:
                    new_line = new_line.replace(puntuation,"")
                new_lyrics+=new_line
            #print(new_lyrics)
            with open(file_location,"w") as new:
                new.write(new_lyrics)
    except Exception as e:
        print(e)
        
# FUNCTION TO READ ALL TEXT FROM A TEXT FILE
def read_lyrics_from_file(file_location_):
    replace(file_location_)
    lyrics_str=""
    try:
        with open(file_location_,'r') as lyrics:
            for line in lyrics:
                lyrics_str+=line
            return lyrics_str
    except Exception as e:
        print(e)
        
# THIS FUNCTION RETURNS AN ARRAY OF ALL WORDS PRESENT IN A TEXT FILE SEPERATED BY SPACES AND \n
def get_words_from_file(file_loc):
    
    try:
        lyrics_lines_arr = np.array(read_lyrics_from_file(file_loc).split("\n"))
        lyrics_word_arr = np.array([])
        for line in lyrics_lines_arr:
            lyrics_word_arr=np.append(lyrics_word_arr,np.array(line.split(" ")))
        return lyrics_word_arr
    except Exception as e:
        print(e)
        
