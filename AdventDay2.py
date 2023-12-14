# Open the file in read mode
import re

with open('c:/Users/JFA3763/Documents/AdventDay2.txt', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.replace("; ",", ")
        gamenumber = re.findall(r'(\S+)\s*(\d+):', line)
        cubelist = re.findall(r'(\d+)\s*(\S+),', line)
        print(gamenumber)
        # Append the line to the list
        lines.append(line)


# Extract key-value pairs from the string using regular expression
key_value_pairs = re.findall(r'(\d+)\s*(\S+)', lines)
 
# Create dictionary from the list of key-value pairs using dictionary comprehension
res = {key: value for key, value in key_value_pairs}
 
# Print the resultant dictionary
print("Resultant dictionary:", res)