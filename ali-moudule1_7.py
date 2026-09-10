def display_string(value):
    try:
        # Check if the exact type is a string
        if not isinstance(value, str):
            raise TypeError
        
        print(value)
        return value
    except TypeError:
        return None

# Examples of how it works:
# print(display_string("Hello World"))  # Displays string, returns "Hello World"
# print(display_string(123))            # Returns None
# print(display_string([1, 2, 3]))      # Returns None
