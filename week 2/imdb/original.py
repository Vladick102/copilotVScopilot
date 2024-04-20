def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    output_set = set()
    key_list = list(film_keywords.keys())
    val_list = list(film_keywords.values())

    for value in film_keywords.values():
        position = val_list.index(value)
        for el in value:
            if el == film_name:
                output_set.add(key_list[position])
    return output_set


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    films_in = {}
    for i in film_keywords.items():
        for j in i[1]:
            if j in films_in:
                films_in[j] += 1
            else:
                films_in[j] = 1

    sorted_keys = sorted_keys = sorted(films_in.items(), key=lambda x: (-x[1], x[0]))
    sorted_final = []
    for el in range(num_of_films):
        sorted_final.append(sorted_keys[el])
    return sorted_final
