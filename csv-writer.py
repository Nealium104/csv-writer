import csv
import io
import os
import re
import readline

def input_rows():
# Open the CSV file in write mode
    with open('output.csv', mode='a', newline='') as file:
        csv_writer = csv.writer(file)

        # If the file empty, set the headers here.
        headers = ['State', 'City', 'Latitude Degrees', '2 1/2 % Design db', 'Heating D.D. Below 65', '2 1/2 % Design db', 'Coincident Design wb', 'Grains Difference 55% RH', 'Grains Difference 50% RH', 'Daily Range']  # Adjust the number of columns as needed
        if os.path.getsize('./output.csv') == 0:
            csv_writer.writerow(headers)

        rows = int(input("State how many rows you want to input at a time. I'd suggest doing this in relevant batches. For example, I'll be doing table 1 by state so I can double check the data. "))
        batch_state_value = input('Name the state for this batch ')
        for row in range(rows):
            # Get user input for each column
            row_data = input_values(headers, batch_state_value)
            rows_remaining = rows - row - 1
            print(f"{row_data}")
            print(f"You have {rows_remaining} rows remaining.")
            # Write the collected inputs as a row in the CSV file
            csv_writer.writerow(row_data)

            # Ask user if they want to add another row
        another = input('Add another batch? (y/n): ')
        if another.lower() == 'y':
            input_rows()

def input_values(headers, state):
    entry = input(f"Enter values for the row. If there are spaces, wrap them in quotes. There should be {len(headers) - 1} values. ")
    reader = csv.reader(io.StringIO(entry), quotechar='"', skipinitialspace=True)
    pattern = r'(?:"([^"]*)"|(\S+))'
    matches = re.findall(pattern, entry)
    row_data = [x[0] if x[0] else x[1] for x in matches]
    row_data.insert(0, state)
    if len(row_data) != len(headers):
        print(row_data)
        print(f"Error: you need to enter exactly {len(headers)} values. If there are values with spaces in them (like New York), make sure you're putting them in quotes. This row was not saved. Please try again. ")
        return input_values(headers, state)
    return row_data

input_rows()
