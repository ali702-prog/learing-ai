from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the time as Seconds:Minutes:Hours
formatted_time = now.strftime("%S:%M:%H")

print(formatted_time)


import datetime

def display_current_minute_fibonacci():
    # 1. Fetch the current date and time
    now = datetime.datetime.now()
    current_min = now.minute
    
    # 2. Define the target length (2 * current minute)
    target_length = 2 * current_min
    
    print(f"Current Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current Minute: {current_min}")
    print(f"Target Sequence Length (2 * {current_min}): {target_length}\n")
    
    # Handle the edge case if the current minute is 0
    if target_length == 0:
        print("Sequence: []")
        return
    
    # 3. Generate the Fibonacci sequence
    # Base case for the first two numbers
    sequence = [0, 1]
    
    # Continue adding terms until the target length is met
    while len(sequence) < target_length:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    # Trim the sequence in the rare event target_length is 1 (e.g. if formula varied)
    # Since 2 * min is always even, sequence will naturally hit the exact length
    final_sequence = sequence[:target_length]
    
    # 4. Display the entire sequence
    print(f"Full Fibonacci Sequence ({target_length} terms):")
    print(final_sequence)

# Run the function
display_current_minute_fibonacci()
