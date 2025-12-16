# allianz-workshop-sdlc-ia
Simple Python code for demonstration purposes.

## Features

This module provides basic arithmetic operations:

### Addition
The `add_numbers(a, b)` function returns the sum of two numbers.

**Usage:**
```python
result = add_numbers(5, 7)
print(result)  # Output: 12
```

### Subtraction
The `subtract_numbers(a, b)` function returns the difference between two numbers.

**Usage:**
```python
result = subtract_numbers(10, 3)
print(result)  # Output: 7
```

### Division
The `divide_numbers(a, b)` function returns the quotient of dividing two numbers.

**Usage:**
```python
result = divide_numbers(20, 4)
print(result)  # Output: 5.0
```

**Note:** Division by zero will raise a `ZeroDivisionError`.

## Parameters

Both functions accept:
- `a` (int | float): First number
- `b` (int | float): Second number

## Returns

- `add_numbers`: Returns the sum (a + b)
- `subtract_numbers`: Returns the difference (a - b)
- `divide_numbers`: Returns the quotient (a / b)

## Testing

Run the test suite with:
```bash
python test.py
```
