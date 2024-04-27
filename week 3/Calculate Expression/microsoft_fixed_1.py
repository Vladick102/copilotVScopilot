"""
The calculate_expression function takes
a single argument - a string with a simple
mathematical expression and returns
an integer - the result of this expression
"""


def calculate_expression(expression: str) -> int | str:
    """
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    if isinstance(expression, str):
        if "Скільки буде" not in expression or "?" not in expression:
            expression = "error"
        expression = expression.replace("Скільки буде ", "")
        expression = expression.replace("поділити на", "/")
        expression = expression.replace("помножити на", "*")
        expression = expression.replace("додати", "+")
        expression = expression.replace("плюс", "+")
        expression = expression.replace("відняти", "-")
        expression = expression.replace("мінус", "-")
        expression = expression.replace("?", "")
        expression = expression.replace(")", "")
        expression = expression.replace("(", "")
        # if len(expression) == 1:
        #     return int(expression)

        list_exp = expression.split(" ")
        for i in range(len(list_exp)):
            i += 0
            for sym in list_exp:
                if sym == "*":
                    pos_element = list_exp.index(sym)
                    if pos_element == len(list_exp) - 1:
                        return "Неправильний вираз!"
                    result = int(list_exp[pos_element - 1]) * int(
                        list_exp[pos_element + 1]
                    )
                    list_exp.pop(pos_element - 1)
                    list_exp.pop(pos_element)
                    list_exp[pos_element - 1] = result
                    break
                if sym == "/":
                    pos_element = list_exp.index(sym)
                    if pos_element == len(list_exp) - 1:
                        return "Неправильний вираз!"
                    if int(list_exp[pos_element + 1]) == 0:
                        return "Неправильний вираз!"
                    result = int(list_exp[pos_element - 1]) / int(
                        list_exp[pos_element + 1]
                    )
                    list_exp.pop(pos_element - 1)
                    list_exp.pop(pos_element)
                    list_exp[pos_element - 1] = result
                    break
                if sym == "+":
                    pos_element = list_exp.index(sym)
                    if pos_element == len(list_exp) - 1:
                        return "Неправильний вираз!"
                    result = int(list_exp[pos_element - 1]) + int(
                        list_exp[pos_element + 1]
                    )
                    list_exp.pop(pos_element - 1)
                    list_exp.pop(pos_element)
                    list_exp[pos_element - 1] = result
                    break
                if sym == "-":
                    pos_element = list_exp.index(sym)
                    if pos_element == len(list_exp) - 1:
                        return "Неправильний вираз!"
                    result = int(list_exp[pos_element - 1]) - int(
                        list_exp[pos_element + 1]
                    )
                    list_exp.pop(pos_element - 1)
                    list_exp.pop(pos_element)
                    list_exp[pos_element - 1] = result
                    break
        try:
            expression = "".join(list_exp)
        except TypeError:
            return list_exp[0]
        return "Неправильний вираз!"
    return "Неправильний вираз!"
