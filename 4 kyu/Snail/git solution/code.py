def snail(array):
    result = []
    while array:
        result += array.pop(0)
        array = list(zip(*array))[::-1]
    return result
