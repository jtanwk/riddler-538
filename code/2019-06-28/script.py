import numpy as np
import pandas as pd
import itertools
import random
import re
from pathlib import Path
import os


# Load scrabble wordlist
WORDLIST_FILE = 'words.txt'
with open(WORDLIST_FILE) as f:
    WORDLIST = set(f.read().split('\n'))

# Make tile string-- @ and # represent two different wildcards
TILES = ('e'*12) + ('ai'*9) + ('o'*8) + ('nrt'*6) + ('lsud'*4) + ('g'*3) + \
        ('bcmpfhvwy'*2) + 'kjxqz@#'

# Make simple scoring dictionary for each letter
LETTER_SCORES = {"a": 1 , "b": 3 , "c": 3 , "d": 2 , "e": 1 ,
                 "f": 4 , "g": 2 , "h": 4 , "i": 1 , "j": 8 ,
                 "k": 5 , "l": 1 , "m": 3 , "n": 1 , "o": 1 ,
                 "p": 3 , "q": 10, "r": 1 , "s": 1 , "t": 1 ,
                 "u": 1 , "v": 4 , "w": 4 , "x": 8 , "y": 4 ,
                 "z": 10}

# Make random tilestring
def get_tilestring(tiles):
    '''Samples without replacement from tiles, then joins output list back
    into a string and returns result.'''
    return ''.join(random.sample(tiles, k=len(tiles)))


# Function to find all possible n-grams of each length
# Adapted from http://www.locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
def get_ngrams(input_string, n, min_length=2, wordlist=WORDLIST):
    '''
    Returns a set of all valid ngrams up to max length n from an input word.
    Leaves in ngrams with wildcards.
    '''
    # Create and join ngrams in a set
    result = set()
    for i in range(min_length, n):
        tuple_list = list(zip(*[input_string[x:] for x in range(i)]))
        ngram_list = [''.join(x) for x in tuple_list]
        result.update(ngram_list)

    # Filter out nonvalid words, but leave in wildcard ngrams
    wildcard_ngrams = {x for x in result if '#' in x or '@' in x}
    non_wildcard_ngrams = wordlist.intersection(result)

    return wildcard_ngrams.union(non_wildcard_ngrams)

# Make simple scoring functions for each case
def score_word(input_word, scoring_dict=LETTER_SCORES):
    '''Applies scoring_dict() for each letter and returns the sum total.'''
    return sum([scoring_dict[x] for x in input_word])


def score_set(input_set):
    '''Scores all words in the sets and returns the sum total.'''
    return sum(list(map(score_word, input_set)))


def score_wildcard_set(input_set, wordlist=WORDLIST):

    sub_options = list(itertools.product([chr(97 + x) for x in range(26)], repeat=2))
    sub_scores = []

    for i, j in sub_options:
        substituted = {x.replace('@', i).replace('#', j) for x in input_set}.intersection(wordlist)
        sub_scores.append(score_set(substituted))

    best_score, best_sub = sorted(zip(sub_scores, sub_options))[-1]

    return best_score

# Make wrapper scoring function to handle all cases
def get_score(input_set, wordlist=WORDLIST):
    '''
    Applies score_word to every element of input_set and returns the total.
    '''
    # Score non-wildcard words
    non_wild_words = {x for x in input_set if '@' not in x and '#' not in x}
    non_wild_sum = score_set(non_wild_words)

    # Score wildcard words
    wild_words = {x for x in input_set if '@' in x or '#' in x}
    wild_sum = score_wildcard_set(wild_words)

    return non_wild_sum + wild_sum


def main():

    NUM_TRIALS = 10^6
    LOG_FILE = 'tiles.txt'

    # LOOP
    best_score = 0
    best_tileset = ''
    for i in range(NUM_TRIALS):
        tiles = get_tilestring(TILES)
        ngrams = get_ngrams(tiles, 15)
        score = get_score(ngrams)

        if score > best_score:
            best_score = score
            best_tileset = tiles

        print('Generating %d out of %d tilesets' % (i+1, NUM_TRIALS), end='\r')

    # SAVE RESULTS
    if not os.path.exists(LOG_FILE):
        Path(LOG_FILE).touch()
    else:
        os.remove(LOG_FILE)
        Path(LOG_FILE).touch()

    with open(LOG_FILE, 'w') as f:
        f.write('BEST TILESET: ' + best_tileset + '\n')
        f.write('BEST SCORE: ' + str(best_score))


if __name__ == "__main__":
    main()
