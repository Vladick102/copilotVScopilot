def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    return {key for key, value in film_keywords.items() if film_name in value}


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    films_in = {}
    for keywords in film_keywords.values():
        for film in keywords:
            films_in[film] = films_in.get(film, 0) + 1

    sorted_films = sorted(films_in.items(), key=lambda x: (-x[1], x[0]))
    return sorted_films[:num_of_films]
