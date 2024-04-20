"""
IMDB Task
"""
def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    finds films with the most keywords
    >>> find_film_keywords({
    ... 'historic': ['Film1', 'Film3'],
    ... 'tragedy': ['Film1', 'Film2'],
    ... 'sientific': ['Film1', 'Film2', 'Film5'],
    ... 'comedy': ['Film2', 'Film4'],
    ... }, 'Film3')
    {'historic'}
    """
    return {keyword for keyword, films in film_keywords.items() if film_name in films}

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    finds films with the most keywords
    >>> find_films_with_keywords({
    ... 'historic': ['Film1', 'Film3'],
    ... 'tragedy': ['Film1', 'Film2'],
    ... 'sientific': ['Film1', 'Film2', 'Film5'],
    ... 'comedy': ['Film2', 'Film3'],
    ... 'series': ['Film2', 'Film3']
    ... }, 3)
    [('Film2', 4), ('Film1', 3), ('Film3', 3)]
    """
    films_count = {}
    for films in film_keywords.values():
        for film in films:
            films_count[film] = films_count.get(film, 0) + 1

    sorted_films = sorted(films_count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_films[:num_of_films]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())