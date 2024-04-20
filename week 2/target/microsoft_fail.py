import random

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    """
    consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    vowels = ['A','E','I','O','U','Y']
    a = [random.choice(vowels) for _ in range(3)] + [random.choice(consonants) for _ in range(6)]
    return [[a.pop(random.choice(range(len(a)))) for _ in range(3)] for _ in range(3)]

def is_valid_word(word: str, letters: list[str]) -> bool:
    """
    Checks if a word is valid according to the game rules.
    """
    if len(word) not in range(4, 10) or letters[4] not in word:
        return False
    letters_set = set(letters)
    return all(sym in letters_set for sym in word)

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()[3:]
        return [word.rstrip().lower() for word in lines if is_valid_word(word, letters)]

def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    """
    try:
        return [input() for _ in iter(int, 1)]
    except EOFError:
        return []

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    return [word.lower() for word in user_words if word not in words_from_dict and is_valid_word(word, letters)]

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
