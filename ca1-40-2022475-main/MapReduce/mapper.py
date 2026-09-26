#!/usr/bin/env python3
import sys
import csv

# Read from standard input (used by Hadoop streaming)
reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        # Extract relevant fields from the CSV row
        station = row['WaterbodyName'].strip()   # Name of the monitoring station
        date    = row['SampleDate'].strip()      # Full date, format: YYYY-MM-DD
        ph      = row['pH'].strip()              # pH value as a string

        # Check that none of the required values are empty
        if station and date and ph:
            # Extract only the year and month part from the date
            month = date[:7]  # Format: "YYYY-MM"
            # Emit key-value pair: station|month and pH
            print(f"{station}|{month}\t{ph}")
    except KeyError:
        # Skip rows missing expected columns (e.g., header or malformed lines)
        continue