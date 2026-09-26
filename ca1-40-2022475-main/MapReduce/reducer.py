#!/usr/bin/env python3
import sys

# Initialize variables for tracking the current key and pH statistics
current_key = None
sum_ph = 0.0
count = 0

# Process each line from standard input (key \t value)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    # Split the line into key and value
    key, value = line.split('\t', 1)
    try:
        ph = float(value)  # Convert pH value to float
    except ValueError:
        continue  # Skip invalid numeric values

    # If the key is the same as the previous one, accumulate the pH value
    if key == current_key:
        sum_ph += ph
        count += 1
    else:
        # When the key changes, calculate and emit the average for the previous key
        if current_key is not None:
            avg = sum_ph / count
            print(f"{current_key}\t{avg:.2f}")
        # Reset tracking variables for the new key
        current_key = key
        sum_ph = ph
        count = 1

# Emit the average for the last group
if current_key is not None:
    avg = sum_ph / count
    print(f"{current_key}\t{avg:.2f}")