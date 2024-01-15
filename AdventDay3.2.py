import re

with open("AdventDay3Puzzle.txt") as f:
    data = f.read().splitlines()

result = 0
gears_found = []

for row_number, row in enumerate(data):
    gears = re.finditer(r'[\*]', row)
    previous_row = data[row_number - 1] if row_number > 0 else '............................................................................................................................................'
    next_row = data[row_number + 1] if row_number < len(data) - 1 else '............................................................................................................................................'
    for match in gears:
        gear_position = match.end()
        adjusted_start = max(0, gear_position - 1)
        adjusted_end = min(len(row), gear_position +1)
        perimeter_range = [
            previous_row,
            row,
            next_row
        ]
        gear_ratio_list = []
        for line in perimeter_range:
            numbers = re.finditer(r'\d+', line)
            for number in numbers:
                if adjusted_start <= number.start()+1 <= adjusted_end or adjusted_start <= number.end() <= adjusted_end:
                    gear_ratio_list.append(int(number.group()))
                else:
                    continue
        if len(gear_ratio_list) == 2:
            result += gear_ratio_list[0]*gear_ratio_list[1]
        else:
            continue
print(result)