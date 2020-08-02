from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import csv
import json
import re

# file containing artists - songs mapping
songs_json = "Artists-Songs Mapping.json"
songs_dict = {}

with open(songs_json) as file:
    songs_dict = json.load(file)
    
# artist for which the lyrics need to be written
artist = "eminem"
songs = songs_dict[artist]
processed_songs = []

# preprocessing the songs name for scraping
for song in songs:
    numbers_in_brackets_removed = re.sub(r'\(.*\)',"",song)
    processed_song = re.sub(r'\W+', '', numbers_in_brackets_removed).lower()
    processed_songs.append(processed_song)
    
print(len(processed_songs))

# Removing duplicate songs
processed_songs = list(set(processed_songs))
print(len(processed_songs))
print(processed_songs[:20])

# url to scrape the lyrics from
base_url = "https://www.azlyrics.com/lyrics/{}/{}.html"

# file in which the lyrics would be saved
lyrics_file = "lyrics_scraped.txt"

lyrics_not_found_for = []

# delay after each execution of call for not exceeding the requests count and also not to overburden the server
delay = 10

with open(lyrics_file, "w") as file:
    
    for song in processed_songs:
        final_url = base_url.format(artist,song)

        try:
            html_page = urlopen(final_url)
            soup = BeautifulSoup(html_page, 'html.parser')

            html_pointer = soup.find('div', attrs={'class':'ringtone'})
            song_name = html_pointer.find_next('b').contents[0].strip()
            lyrics = html_pointer.find_next('div').text.strip()

            file.write("###"+song_name+"###")
            file.write("\n\n")
            file.write(lyrics)
            file.write("\n\n")
            
            print("Lyrics successfully written to file for : " + song_name)
            
        except:
            print("Lyrics not found for : " + song)
            lyrics_not_found_for.append(song)
            
        finally:
            sleep(delay)
            
print("Total count : ", len(songs),"songs")
print("Lyrics successfully scraped for : ", len(songs)-len(lyrics_not_found_for), "songs")
print("Lyrics not found for :", len(lyrics_not_found_for),"songs\n")
print("\nHere's the list :\n")
print(lyrics_not_found_for)
