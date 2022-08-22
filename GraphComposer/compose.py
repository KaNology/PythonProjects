"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)

        # Turn whitespaces between words into a single space
        text = ' '.join(text.split())
        text = text.lower()
        # Remove punctuations such as ! @ # $ , . and more
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() # Split on spaces again

    # words = words[:1000]

    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # For each word
    for word in words:
        # Check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # If there was a previous word (that is followed by this word)
        # , then add an edge if does not exist.
        # If exists, increment weight by 1.
        if prev_word:  # Prev word should be a Vertex
            # Check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=50):
    composition = []
    # Pick a random word in the Graph to start
    word = g.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    words = get_words_from_text('GraphComposer/texts/hp_sorcerer_stone.txt')

    # for song in os.listdir('songs/{}'.format(artist)):
        # if song == '.DS_Store':
        #     continue
        # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))
        
    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()