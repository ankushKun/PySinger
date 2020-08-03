from gtts import gTTS


def sing(file_name):
    LYRICS = ""
    with open(f'./generated_lyrics/{file_name}','r') as l:
        LYRICS = l.read()
    print(LYRICS)
    tts = gTTS(LYRICS)
    tts.save(f'./generated_lyrics/{file_name.replace(".txt",".mp3")}')
    

sing('test.txt')
