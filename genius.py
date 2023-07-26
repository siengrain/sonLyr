from bs4 import BeautifulSoup
import requests
from requests import get

def deletebw(input_string, start_word, end_word):
    start_index = input_string.find(start_word)
    end_index = input_string.find(end_word)

    if start_index == -1 or end_index == -1:
        return input_string

    output_string = input_string[:start_index] + input_string[end_index + len(end_word):]

    return output_string

def getLyrics(link):
    w = requests.get(link)
    if w:
        soup = BeautifulSoup(w.text, 'html.parser')
        lyr = soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-5 Dzxov")
        let = str(lyr)
        let = let.replace("<br/>","\n")
        let = parsero('[', ']', let)
        let = parsero('<', '>', let)
        let = let.replace('[','')
        let = let.replace(']','')
        return(let)
    else:
        error = "\nCouldn't find that song"
        return error

def parsero(word1, word2, lyrics):
    while word1 in lyrics:
        lyrics = deletebw(lyrics, word1, word2)
    return lyrics
