import re
import itertools

with open("AdventDay4Puzzle.txt") as f:
    data = f.read().splitlines()

result = 0
card_value = 0

for row in data:
    row = row.split(': ')
    removed_game = row.pop(0)
    row = ''.join(row)
    row = row.split(' | ')
    scratch_numbers = ''.join(row[0])
    scratch_numbers = re.finditer(r'\d+', scratch_numbers)
    winning_numbers = ''.join(row[1])
    winning_numbers = re.findall(r'\d+', winning_numbers)
    print(winning_numbers)
    winning_numbers_found = 0
    for number in scratch_numbers:
        number = number.group()
        print(number)
        if number in winning_numbers:
            winning_numbers_found += 1
            if winning_numbers_found == 1:
                card_value += 1
            else:
                card_value = card_value*2
            print("found")
    result += card_value
    card_value = 0
print(result)
