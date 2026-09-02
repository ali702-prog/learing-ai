def check_even_odd(number):
    """Returns whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Examples of using the function
print(check_even_odd(4))   # Output: Even
print(check_even_odd(7))   # Output: Odd
print(check_even_odd(-2))  # Output: Even
