'''Target game'''

import random

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    >>> random.seed(1)
    >>> generate_grid()
    [['L', 'U', 'T'], ['E', 'T', 'Q'], ['S', 'A', 'F']]
    """
    consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    vowels = ['A','E','I','O','U','Y']
    a = []
    for i in range(3):
        a.append(random.choice(vowels))
        i+=1
    for i in range(6):
        a.append(random.choice(consonants))
    small_list = []
    big_list = []
    for i in range(3):
        for b in range(3):
            x = random.choice(a)
            small_list.append(x)
            a.remove(x)
            b += 1
        big_list.append(small_list)
        small_list = []
    return big_list


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
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_list = []
    try:
        while True:
            x = input()
            user_list.append(x)
    except EOFError:
        return user_list

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str])\
 -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['banana', 'aaaan'],['b','a','n','a','n','a','a','a','a'], ['banana'])
    ['aaaan']
    """
    pure_words = []
    for word in user_words:
        if len(word) in range(4, 10) and word not in words_from_dict  and letters[4] in word:
            letters2 = letters[:]
            k = 0
            for sym in word.lower():
                if sym in letters2:
                    k += 1
                    letters2.remove(sym)
            if k == len(word):
                pure_words.append(word.lower())
    return pure_words

def main():
    """
    Starts the game.
    """
    board = generate_grid()
    letters = []
    for i in board:
        letters.extend(i)
    for a,b in enumerate(letters):
        letters[a] = b.lower()
    print('Your board is ' + str(board))
    print('Please, suggest your words here:')
    user_words = get_user_words()
    words_from_dict = get_words('en', letters)
    pure_words = get_pure_user_words(user_words, letters, words_from_dict)
    missed_words = []
    for x in words_from_dict:
        if x not in user_words:
            missed_words.append(x)
    print('Number of the right words: ' + str(len(user_words) - len(pure_words)))
    print('All possible words:')
    print(words_from_dict)
    print('You missed the following words:')
    print(missed_words)
    print("You suggest, but we don't have in the dictionary:")
    print(pure_words)