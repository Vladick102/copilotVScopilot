# ****************************************
# Problem 1
# ****************************************
def get_position(ch: str):
    """
        str -> int or None
    Return the position of a letter in the alphabet. If the argument is not a letter, the function should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')
    None
    """
    if isinstance(ch, str):
        if len(ch) == 1:
            if 'A' <= ch <= 'Z':
                return ord(ch) - ord('A') + 1
            elif 'a' <= ch <= 'z':
                return ord(ch) - ord('a') + 1
        else:
            return None




# ****************************************
# Problem 2
# ****************************************
    
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """
    if isinstance(ch1, str) and isinstance(ch2, str):
        if len(ch1) == 1 and len(ch2) == 1 and ('A' <= ch1 <= 'Z' or 'a' <= ch1 <= 'z') and ('A' <= ch2 <= 'Z' or 'a' <= ch2 <= 'z'):
                    if len(ch1) == 1 and len(ch2) == 1:
                       if ch1.lower() > ch2.lower():
                        return True
                       else:
                        return False
    else:
     return



# ****************************************
# Problem 3
# ****************************************


def compare_str(s1, s2):
  """
  (str, str) -> bool
  Compare two srings lexicographicly. Return True if string s1 is larger
  than string s2 and False otherwise. If arguments aren't string or function
  have different length function should return None.

  >>> compare_str('abc', 'Abd')
  False
  >>> compare_str('zaD', 'zab')
  True
  >>> compare_str('zaD', 'Zad')
  False
  >>> compare_str('aaa', 'aaaaa')

  >>> compare_str('2015', 2015)

  """
  if isinstance(s1, str) and isinstance(s2, str):
        if len(s1) == len(s2):
            return s1 < s2
        else:
            return None
  return None
# ****************************************
# Problem 4
# ****************************************
def type_by_angles(a: float, b: float, c: float):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    acute triangle
    >>> type_by_angles(90, 30, 60)
    right angled triangle
    >>> type_by_angles(2015, 2015, 2015)

    """
    if a + b + c == 180  and a > 0 and b > 0 and c > 0:
        if a == 90 or b == 90 or c == 90:
            return "right-angled triangle"
        elif a > 90 and b > 90 and c >90:
            return "obtuse triangle"
        else:
            return "acute triangle"
    else:
        return None


# ****************************************
# Problem 5
# ****************************************

def type_by_sides(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    "acute triangle"
    >>> type_by_sides(3, 4, 5)
    "right angled triangle"
    >>> type_by_sides(3, 3, 2015)
    """
    if a + b > c and a + c > b and b + c > a:
        sides = [a, b, c]
        sides.sort() 
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            return "right-angled triangle"
        elif sides[0]**2 + sides[1]**2 < sides[2]**2:
            return "obtuse triangle"
        else:
            return "acute triangle"
    else:
        return None


# ****************************************
# Problem 6
# ****************************************
def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    """
    if isinstance(s, str):
        word = ''
        for ch in s:
            if ch != ' ':
                word += ch
            else:
                print(word)
                word = ''
    else:
        return None


# ****************************************
# Problem 7
# ****************************************
def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    if isinstance(s, str):
        sentence = 0

        for char in s:
            if char in ('.', '!', '?'):
              sentence += 1  
        return sentence
    else:
        return None
# ****************************************
# Problem 8
# ****************************************

def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    ****************************************************
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    **************************************************
    >>> number_of_sentences(2015)

    """
    if isinstance(s, str):
         text = ''
         for char in s:
            print('*', end="")
         return text
    else:
     return None

# ****************************************
# Problem 9
# ****************************************

def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    Revenge is a dish that tastes best when served cold.
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    Never hate your enemies. It affects your judgment.
    >>> decrypt_message(2015)

    """
    if isinstance(s, str):
        checked=''
        for char in s:
            if ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
                print(char, end='')
            else:
              print(chr(ord(char) - 1), end='')
        return checked
              
    else:
        return None

# ****************************************
# Problem 10
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    if isinstance(s1, str) and isinstance(s2, str):
        text = ""
        for char in s1:
            if char not in s2:
                text += char  
        return text
    else:
        return None


# ****************************************
# Problem 11
# ****************************************
def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    pass
    if isinstance(lst, list) and len(lst) == 26:
        text = ""
        for i in range(26):
            if not isinstance(lst[i], int) or lst[i] < 0:
                return None
            text += chr(ord('a') + i) * lst[i]
        return text
    else:
        return None
# ****************************************
# Problem 12
# ****************************************
def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    a
    >>> get_letters(-2015)

    """
    pass


# ****************************************
# Problem 13
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    pass


# ****************************************
# Problem 14
# ****************************************
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    abc
    >>> find_union("aZAbc", "zzYYxp")
    AYZabcpxz
    >>> find_union("sfdfsdf", 2015)

    """
    pass


# ****************************************
# Problem 15
# ****************************************
def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    if not isinstance(lst, list) or not isinstance(s, str):
            return None

    count = 0
    for word in lst:
        for char in word:
            if ord(char) == ord(s):
              count += 1
    return count
   

# ****************************************
# Problem 16
# ****************************************

def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_occurence("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    count = 0
    if isinstance(s, str):
        for char in s:
            if 65 <= ord(char)  <= 90:
                count += 1
        return count
    else:
        return None
# ****************************************
# Problem 17
# ****************************************

def polynomial_eval(coefficients, value):
    """
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    count = 0
    power = len(coefficients) - 1

    for c in coefficients:
        count += c * pow(value, power)
        power -= 1

    return count


# ****************************************
# Problem 18
# ****************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """

    return True


# ****************************************
# Problem 19
# ****************************************
def one_swap_sorting(sequence):
    """
    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """

    return True


# ****************************************
# Problem 20
# ****************************************
def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    return True


# ****************************************
# Problem 21
# ****************************************
def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """

    return True


# ****************************************
# Problem 22
# ****************************************
def sum_of_divisors(n, lst):
    """
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    pass


# ****************************************
# Problem 23
# ****************************************
def turn_over(n, lst):
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> reverse(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> reverse(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> reverse(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse(-5, [])
    []

    """
    pass



# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())

