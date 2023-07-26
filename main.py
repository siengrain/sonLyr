#!/usr/bin/env python3 
import genius

r = ''

dic = {'á':'a', 'é':'e', 'í':'i','ó':'o','ú':'u',' ':'-'}


def replaceChar(input_string, char_replacement_dict):
    output_string = ""

    for char in input_string:
        if char in char_replacement_dict:
            output_string += char_replacement_dict[char]
        else:
            output_string += char

    return output_string

def getLink(song, author):
    song = song.lower()
    song = replaceChar(song, dic) 
    author = author.lower()
    author = author.capitalize()
    author = replaceChar(author, dic)

    base_url = f"https://genius.com/{author}-{song}-lyrics"
    return base_url
    

while r != 'q':
    song = input("Name of the song: ")
    author = input("Name of the artist: ")
    link = getLink(song, author)
    lyrics = genius.getLyrics(link)
    print("\n")
    print(lyrics)
    print("\n")
    r = input("\n\nType q to quit, anything else to search a different song: ");
