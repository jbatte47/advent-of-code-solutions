# Open the file in read mode
with open('./AdventDay1Puzzle.txt', 'r') as file:
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
    replaced_string = l.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')
    all_numbers = re.findall(r'\d', replaced_string)
    first_number = all_numbers[0]
    last_number = all_numbers[-1]
    number = first_number + last_number
    number = int(number)
    final.append(number)
print(sum(final))