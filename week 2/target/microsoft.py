"""
This module contains a word game where the player sees a game board with 9 letters.
The task of the player is to find as many words as possible that consist of four or more letters.
Each letter can appear in the word as many times as it appears on the game board.
Each word must contain the central letter.
"""
# import time
import random
# start = time.time()
import tracemalloc
tracemalloc.start()
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    """
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    a = [random.choice(vowels) for _ in range(3)] + [random.choice(consonants) for _ in range(6)]
    return [[a.pop(random.choice(range(len(a)))) for _ in range(3)] for _ in range(3)]



def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en', ['a','b','c','d','e','f','g','h','i'])
    ['cafh', 'chafe', 'chef', 'chief', 'deaf', 'face', 'faced', 'fade', 'fadge', 'fage', 'fice', \
'fiche', 'fide', 'fidge', 'heaf']
    """
    word_list = []
    with open(f, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        del lines[:3]
        for word in lines:
            word = (word.rstrip()).lower()
            if len(word) in range(4,10) and letters[4] in word:
                letters2 = letters[:]
                k = 0
                for sym in word:
                    if sym in letters2:
                        letters2.remove(sym)
                        k += 1
                if k == len(word):
                    word_list.append(word)
    return word_list

def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    """
    user_list = []
    try:
        while True:
            user_list.append(input())
    except EOFError:
        return user_list

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    for word in user_words:
        word = word.lower()
        if len(word) in range(4, 10) and word not in words_from_dict and letters[4] in word:
            letters2 = letters[:]
            if all(sym in letters2 for sym in word):
                pure_words.append(word)
                for sym in word:
                    letters2.remove(sym)
    return pure_words

def main():
    """
    Starts the game.
    """
    board = generate_grid()
    letters = [b.lower() for i in board for b in i]
    print('Your board is', board)
    print('Please, suggest your words here:')
    user_words = get_user_words()
    words_from_dict = get_words('en', letters)
    pure_words = get_pure_user_words(user_words, letters, words_from_dict)
    missed_words = [x for x in words_from_dict if x not in user_words]
    print('Number of the right words:', len(user_words) - len(pure_words))
    print('All possible words:')
    print(words_from_dict)
    print('You missed the following words:')
    print(missed_words)
    print("You suggest, but we don't have in the dictionary:")
    print(pure_words)

get_words('en.txt', ['a','b','c','d','e','f','g','h','i'])
# end = time.time()
# print(end-start)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()