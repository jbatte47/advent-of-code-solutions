import re

with open("AdventDay3Puzzle.txt") as f:
    data = f.read().splitlines()

result = 0
print(result)

for row_number, row in enumerate(data):
    numbers = re.finditer(r'\d+', row)
    previous_row = data[row_number - 1] if row_number > 0 else None
    next_row = data[row_number + 1] if row_number < len(data) - 1 else None
    for match in numbers:
        number = int(match.group())
        adjusted_start = max(0, match.start() - 1)
        adjusted_end = min(len(row), match.end() +1)
        perimeter_range = [
            previous_row[adjusted_start:adjusted_end] if previous_row is not None else '.....',
            row[adjusted_start:adjusted_end],
            next_row[adjusted_start:adjusted_end] if next_row is not None else '.....'
        ]
        print(result)
        print(f"ROW NUMBER: {row_number}")
        print(perimeter_range)
        if any(not ch.isdigit() and ch != '.' for item in perimeter_range for ch in item) == True:
            print(result)
            print(number)
            result += number
            print(result)
        else:
            continue

"""PSEUDOCODE:
Use group() to find the index range of all digits in a line
Check the positions to the left and to the right of the digit in question
Check the line above and below for the same index range +1 and -1.

I was going to use a set to push it into if it found a "fun" character within the range 
but if the same number ever shows on the same line or later on that can't work

Instead, put the returned digit ranges in a loop and 
force it to add to a variable then break/move onto the next number if it finds a match on the "fun" symbols (not a number or a ".")
"""