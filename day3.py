import re

def day3_1():
  with open('./day3_advent_input.txt', 'r') as input:
    lines = input.readlines()
    char_map = [list(line.strip()) for line in lines]

    def is_catalog_num(row, line_len, match_text, match_start):
      text_len = len(match_text)
      col_range = range(match_start - 1, match_start + text_len + 1)
      top_row = [(row - 1, col) for col in col_range]
      middle_row = [(row, match_start - 1), (row, match_start + text_len)]
      bottom_row = [(row + 1, col) for col in col_range]
      def is_content_char(x, y):
        if x >= 0 and x < len(char_map) and y >= 0 and y < line_len:
          return char_map[x][y] != '.'
        return False
      matches = [True for x, y in top_row + middle_row + bottom_row if is_content_char(x, y)]
      return len(matches) > 0

    catalog_nums = [
      int(match.group())
      for (row_num, line) in enumerate(lines)
      for match in re.finditer('\d+', line)
      if is_catalog_num(row_num, len(line) - 1, match.group(), match.start())
    ]

    return sum(catalog_nums)

def day3_2():
  with open('./day3_advent_input.txt', 'r') as input:
    lines = input.readlines()

    def get_gear_ratio(row_num, col_num):
      target_lines = [
        (row_num - 1, lines[row_num - 1] if row_num > 0 else None),
        (row_num, lines[row_num]),
        (row_num + 1, lines[row_num + 1] if row_num < len(lines) else None)
      ]
      matching_parts = [
        (index, int(match.group()))
        for index, line in target_lines if line is not None
        for match in re.finditer('\d+', line)
        for match_col in range(*match.span()) if match_col in range(col_num - 1, col_num + 2)
      ]
      unique_parts = list(set(matching_parts))
      return unique_parts[0][1] * unique_parts[1][1] if len(unique_parts) == 2 else 0

    gear_ratios = [
      get_gear_ratio(row_num, match.start())
      for row_num, line in enumerate(lines)
      for match in re.finditer('\*', line)
    ]

    return sum(gear_ratios)
