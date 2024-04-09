def square_digits(number):
    # Convert the number to a string to extract individual digits
    num_str = str(number)
    
    # Initialize an empty string to store the concatenated squared digits
    result = ""
    
    # Iterate through each digit in the number
    for digit in num_str:
        # Square the digit and convert it back to an integer
        squared_digit = int(digit) ** 2
        # Append the squared digit to the result string
        result += str(squared_digit)
    
    # Convert the concatenated string back to an integer
    return int(result)