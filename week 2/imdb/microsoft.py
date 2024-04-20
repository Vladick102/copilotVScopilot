def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    return {keyword for keyword, films in film_keywords.items() if film_name in films}


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    films_count = {}
    for films in film_keywords.values():
        for film in films:
            films_count[film] = films_count.get(film, 0) + 1

    sorted_films = sorted(films_count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_films[:num_of_films]
