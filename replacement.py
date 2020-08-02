# VARIABLES
puntuations = ['.',',','"',"'",'!','*',';','-','(',')']

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
        
def get_words_list_from_file(file_loc):
    try:
        lyrics_lines_lst = read_lyrics_from_file(file_loc).split("\n")
        lyrics_word_lst = []
        for line in lyrics_lines_lst:
            lyrics_word_lst += line.split()
        return lyrics_word_lst
    except Exception as e:
        print(e)
