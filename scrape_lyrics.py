from pylyrics3 import *
import os

artist = input("Artist Name : ")
print("Getting lyrics (Its goonna take some time, so grab some stuff to eat)")
em = get_artist_lyrics(artist)

os.mkdir(f'./{artist}')

for name in em.keys():
    try:
        with open(f"./{artist}/{name}.txt","w") as f:
            f.write(em[name])
    except Exception as e:
        print(e)
