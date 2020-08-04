from espeakng import ESpeakNG
es = ESpeakNG()

def sing(file_name):
    LYRICS = ""
    with open(f'./generated_lyrics/{file_name}','r') as l:
        LYRICS = l.read()
    print(LYRICS)
    es.say(LYRICS)
    

sing('test.txt')
