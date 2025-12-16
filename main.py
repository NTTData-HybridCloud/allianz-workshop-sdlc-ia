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

# Main execution
if __name__ == "__main__":
    result = add_numbers(5, 7)
    print(f"The sum of 5 and 7 is: {result}")
