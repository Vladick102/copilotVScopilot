# ****************************************
# Problem 1
# ****************************************
'''
str -> int
Return positon of letter in alphabet. If argument is not a letter function
should return None.
'''
def get_position(character: str) -> int:
    """
    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')
    
    >>> get_position(1)

    """
    if isinstance(character, str):
        if len(character) == 1:
            if 91 > ord(character) > 64:
                return ord(character) - 64
            if 123 > ord(character) > 96:
                return ord(character) - 96
            return None
        return None
    return None

# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1: str, ch2: str) -> bool:
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

    >>> compare_char('sdads', 'TEs')
    
    """
    if isinstance(ch1, str) and isinstance(ch2, str):
        if len(ch1) == len(ch2) == 1:
            return get_position(ch1) > get_position(ch2)
        return None
    return None

# ****************************************
# Problem 3
# ****************************************
def compare_str(s_1: str, s_2: str) -> bool:
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
    if isinstance(s_1, str) and isinstance(s_2, str):
        length_1 = len(s_1)
        length_2 = len(s_2)
        if length_1 != length_2:
            return None
        if s_1 == s_2:
            return False
        if s_1 > s_2:
            return False
        if s_1 < s_2:
            return True
    return None

# ****************************************
# Problem 4
# ****************************************
def type_by_angles(first_angle: float, second_angle: float, third_angle:float) -> str:
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obtuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    >>> type_by_angles(90, 0, 90)
    
    """
    if first_angle + second_angle + third_angle == 180:
        if first_angle != 0 and second_angle != 0 and third_angle != 0:
            if first_angle == 90 or second_angle == 90 or third_angle == 90:
                return 'right angled triangle'
            if first_angle < 90 and second_angle < 90 and third_angle < 90:
                return 'acute triangle'
            if first_angle > 90 or second_angle > 90 or third_angle > 90:
                return 'obtuse triangle'
            return None
        return None
    return None

# ****************************************
# Problem 5
# ****************************************
def type_by_sides(side_1: int, side_2: int, side_3: int) -> str:
    """
    (int, int, int) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obtuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)

    """

    if isinstance(side_1, int) and isinstance(side_2, int) and isinstance(side_3, int):

        unsorted_sides = [side_1, side_2, side_3]
        sides = sorted(unsorted_sides)

        if sides[0] + sides[1] > sides[2]:
            if (sides[0] ** 2) + (sides[1] **2) == (sides[2] ** 2):
                return 'right angled triangle'
            if (sides[0] ** 2) + (sides[1] **2) < (sides[2] ** 2):
                return 'obtuse triangle'
            if sides[0] == sides[1] == sides[2]:
                return 'acute triangle'
            return None
        return None
    return None

# ****************************************
# Problem 6
# ****************************************
def convert_to_column(input_string):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.
    >>> convert_to_column(2015)
    """
    column = ''
    if isinstance(input_string, str):
        input_string = input_string.replace('.', '')
        input_string = input_string.lower()
        list_s = input_string.split()
        length = len(list_s)
        for i in range(length):
            column += list_s[i] + '\n'
        return column[:-1]
    return None
# ****************************************
# Problem 7
# ****************************************
def number_of_sentences(string: str) -> int:
    """
    str -> int
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    if isinstance(string, str):
        list_s = string.split('.')
        return len(list_s) - 1
    return None

# ****************************************
# Problem 8
# ****************************************
def replace_with_stars(string: str) -> str:
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> replace_with_stars("Revenge is a dish that tastes best when served cold.")
    '****************************************************'
    >>> replace_with_stars("Never hate your enemies. It affects your judgment.")
    '**************************************************'
    >>> replace_with_stars(2015)

    """
    if isinstance(string, str):
        length = len(string)
        return '*' * length
    return None

# ****************************************
# Problem 9
# ****************************************
def decrypt_message(string: str) -> str:
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    """
    if isinstance(string, str):
        decrypted_string = ''
        for i in string:
            if i not in (' ', '.'):
                good_letter = chr(ord(i) - 1)
                decrypted_string += good_letter
            elif i == ' ':
                decrypted_string += i
            elif i == '.':
                decrypted_string += i
        return decrypted_string
    return None

# ****************************************
# Problem 10
# ****************************************
def exclude_letters(string_1: str, string_2: str) -> str:
    """
    (str, str) -> str
    Delete all letter from string string_2 in string string_1.
    If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    'aaa'
    >>> exclude_letters("abcc", "cczzyy")
    'ab'
    >>> exclude_letters(2015, "sasd")

    """
    if isinstance(string_1, str) and isinstance(string_2, str):
        list_1 = list(string_1)
        list_2 = list(string_2)

        for i in list_2:
            while i in list_1:
                list_1.remove(i)
        return ''.join(list_1)
    return None

# ****************************************
# Problem 11
# ****************************************
def create_string(lst: list) -> str:
    """
    list -> str
    Create and return string from histogram of letters.
    If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    'bcc'
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    'aaaazzzz'
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    if isinstance(lst, list) and len(lst) == 26 and min(lst) >= 0:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                     'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x',
                           'y', 'z']
        string = ''
        for number in range(26):
            string += alphabet[number] * lst[number]
        return string
    return None

# ****************************************
# Problem 12
# ****************************************
def get_letters(number: int) -> str:
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    'a'
    >>> get_letters(-2015)

    """
    if isinstance(number, int) and 0 < number < 27:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                     'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x',
                           'y', 'z']
        letters = alphabet[:number]
        string = ''.join(letters)
        return string
    return None

# ****************************************
# Problem 13
# ****************************************
def find_intersection(string_1: str, string_2: str) -> str:
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    if isinstance(string_1, str) and isinstance(string_2, str):

        string_1 = string_1.lower()
        string_2 = string_2.lower()

        list_1 = list(string_1)
        list_2 = list(string_2)
        common_letter = ''
        for i in list_2:
            if i in list_1:
                common_letter += i
        common_list = list(common_letter)
        common_list = set(common_list)
        common_list = sorted(common_list)
        common_string = ''.join(common_list)
        return common_string
    return None

# ****************************************
# Problem 14
# ****************************************
def find_union(string_1: str, string_2: str) -> str:
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if isinstance(string_1, str) and isinstance(string_2, str):

        list_1 = list(string_1)
        list_2 = list(string_2)

        sum_of_lists = list_1 + list_2
        sum_of_lists = set(sum_of_lists)
        sum_of_lists = sorted(sum_of_lists)
        sum_of_lists = ''.join(sum_of_lists)
        return sum_of_lists
    return None

# ****************************************
# Problem 15
# ****************************************
def number_of_occurence(input_list: list, string: str) -> int:
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
    if isinstance(input_list, list) and isinstance(string, str):
        if all(isinstance(element, str) for element in input_list):
            count = 0
            for i in input_list:
                if string in i:
                    count += 1
            return count
        return None
    return None

# ****************************************
# Problem 16
# ****************************************
def number_of_capital_letters(string: str) -> str:
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    if isinstance(string, str):
        list_s = list(string)
        count = 0
        for i in list_s:
            if i.isupper():
                count += 1
        return count
    return None

# ****************************************
# Problem 17
# ****************************************
def polynomial_eval(coefficients: list, value: int) -> int:
    """
    >>> polynomial_eval([2,3,0,4], 4)
    180
    >>> polynomial_eval([6], 42)
    6
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    if isinstance(coefficients, list) and isinstance(value, int):
        polynomial = 0
        power_of_pol = len(coefficients) - 1
        while power_of_pol > -1:
            for k in coefficients:
                polynomial += k * (value ** power_of_pol)
                power_of_pol -= 1
        return polynomial
    return None
    
# ****************************************
# Problem 18
# ****************************************
def pattern_number(sequence):
    """
    pattern number function
    >>> pattern_number([])
    >>> pattern_number([42])
    >>> pattern_number([1,2])
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])
    >>> pattern_number([1,2,3,1,2,3,1])
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    """
    max_length = len(sequence)//2
    for a in range(1, max_length + 1):
        pattern = sequence[:a]
        count = 0

        for b in range(0, len(sequence), a):
            if sequence[b:b + a] == pattern:
                count += 1
            else:
                break
        if count * a == len(sequence):
            return pattern, count
    return None

    



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
    sorted_sequence = sequence[:]
    sorted_sequence.sort()

    swap_count = 0
    for i,k in enumerate(sequence):
        k += 1
        if sequence[i] != sorted_sequence[i]:
            swap_count += 1
    return bool(swap_count == 2)

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
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    
    ulam_sequence = [1, 2]
    while len(ulam_sequence) < n:
        next_number = ulam_sequence[-1] + 1
        while True:
            sum_count = 0
            for i in range(len(ulam_sequence) - 1):
                for j in range(i + 1, len(ulam_sequence)):
                    if ulam_sequence[i] + ulam_sequence[j] == next_number:
                        sum_count += 1
                        if sum_count > 1:
                            break
                if sum_count > 1:
                    break
            if sum_count == 1:
                ulam_sequence.append(next_number)
                break
            next_number += 1
    return ulam_sequence[:n]


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

    def get_next(num):
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit ** 2
            num //= 10
        return total_sum
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1


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
    return sum(x for x in lst if x % 2 != 0 and x % n == 0)


# ****************************************
# Problem 23
# ****************************************
def turn_over(n, lst):
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []

    """
    if n <= 0:
        return []
    elif n > len(lst):
        n = len(lst)
    return lst[:n][::-1] + lst[n:]



# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
