# це код який написав Microsoft Copilot коли я попросила його написати рішення в один рядок
def square_digits(number): return int(''.join(str(int(digit) ** 2) for digit in str(number)))