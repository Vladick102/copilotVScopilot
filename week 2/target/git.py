import random


def generate_grid() -> list[list[str]]:
    consonants = [
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "W",
        "X",
        "Z",
    ]
    vowels = ["A", "E", "I", "O", "U", "Y"]
    a = random.sample(vowels, 3) + random.sample(consonants, 6)
    return [a[i * 3 : i * 3 + 3] for i in range(3)]


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en', ['a','b','c','d','e','f','g','h','i'])
    ['cafh', 'chafe', 'chef', 'chief', 'deaf', 'face', 'faced', 'fade', 'fadge', 'fage', 'fice', \
'fiche', 'fide', 'fidge', 'heaf']
    """
    word_list = []
    with open(f, "r", encoding="utf-8") as file:
        lines = file.readlines()[3:]
        for word in lines:
            word = word.rstrip().lower()
            if 4 <= len(word) <= 9 and letters[4] in word:
                letters_copy = letters[:]
                for char in word:
                    if char in letters_copy:
                        letters_copy.remove(char)
                    else:
                        break
                else:
                    word_list.append(word)
    return word_list


def get_user_words() -> list[str]:
    user_list = []
    try:
        while True:
            user_list.append(input())
    except EOFError:
        return user_list


def get_pure_user_words(
    user_words: list[str], letters: list[str], words_from_dict: list[str]
) -> list[str]:
    return [
        word.lower()
        for word in user_words
        if 4 <= len(word) <= 9
        and word not in words_from_dict
        and letters[4] in word
        and all(c in letters for c in word.lower())
    ]


def main():
    board = generate_grid()
    letters = [char.lower() for sublist in board for char in sublist]
    print("Your board is", board)
    print("Please, suggest your words here:")
    user_words = get_user_words()
    words_from_dict = get_words("en.txt", letters)
    pure_words = get_pure_user_words(user_words, letters, words_from_dict)
    missed_words = [x for x in words_from_dict if x not in user_words]
    print("Number of the right words:", len(user_words) - len(pure_words))
    print("All possible words:")
    print(words_from_dict)
    print("You missed the following words:")
    print(missed_words)
    print("You suggest, but we don't have in the dictionary:")
    print(pure_words)
