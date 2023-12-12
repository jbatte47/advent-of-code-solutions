# Open the file in read mode
with open('c:/Users/JFA3763/Documents/Advent1.txt', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.strip()

        # Append the line to the list
        lines.append(line)

import re

final = []

for l in lines:
    all_numbers = re.findall(r'\d', l)
    first_number = all_numbers[0]
    last_number = all_numbers[-1]
    number = first_number + last_number
    number = int(number)
    final.append(number)
print(sum(final))
