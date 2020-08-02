from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import csv

# url to scrape the songs list from
base_url = "http://www.song-list.net/{}/songs"

# artists list whose songs list is to be made
artists = ["edsheeran", "eminem", "taylorswift", "linkinpark", "drake-2"]

songs_dict = { }    


for artist in artists:
    
    artist_url = base_url.format(artist)
    print("Going to url : ", artist_url)
    
    html_page = urlopen(artist_url)
    soup = BeautifulSoup(html_page, 'html.parser')
    
    songs_list = soup.find('table', attrs={'class':'songs'}).find_all('td', attrs={'id':'songname'})
    
    songs_dict[artist] = []
    
    for song in songs_list:
        song_name = song.text.strip()
        songs_dict[artist].append(song_name)
        
    print("Artist : ", artist)
    print(songs_dict[artist][:5])
        
    sleep(10)


for key,val in songs_dict.items():
    print(key,len(val))

import json
json_file = "Artists-Songs Mapping.json"
with open(json_file, 'w') as file:
    json.dump(songs_dict, file)

with open(json_file) as f:
    a = json.load(f)
    print(a)
