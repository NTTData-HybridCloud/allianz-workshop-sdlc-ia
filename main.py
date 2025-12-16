# Simple Python Demo

def add_numbers(a, b):
    """Return the sum of a and b.

    Parameters
    ----------
    a : int | float
        First addend.
    b : int | float
        Second addend.

    Returns
    -------
    int | float
        Sum of a and b.
    """
    return a + b

def subtract_numbers(a, b):
    """Return the difference of a and b.

    Parameters
    ----------
    a : int | float
        Minuend (number from which another is subtracted).
    b : int | float
        Subtrahend (number to be subtracted).

    Returns
    -------
    int | float
        Difference of a and b (a - b).
    """
    return a - b

def divide_numbers(a, b):
    """Return the quotient of a divided by b.

    Parameters
    ----------
    a : int | float
        Dividend (number to be divided).
    b : int | float
        Divisor (number to divide by).

    Returns
    -------
    float
        Quotient of a divided by b (a / b).

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Main execution
if __name__ == "__main__":
    result = add_numbers(5, 7)
    print(f"The sum of 5 and 7 is: {result}")
    
    result_sub = subtract_numbers(10, 3)
    print(f"The difference of 10 and 3 is: {result_sub}")
    
    result_div = divide_numbers(20, 4)
    printer(f"The division of 20 by 4 is: {result_div}")
