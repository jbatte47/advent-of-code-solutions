import re

max_cubes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

line_pattern = '^Game\s+(?P<number>\d+):\s+(?P<results>.+)$'
reveal_pattern = '(?P<count>\d+)\s+(?P<color>[^,]+)'

def within_threshold(reveal):
  violators = [key for key, value in reveal.items() if key in max_cubes and value > max_cubes[key]]
  return len(violators) == 0

def parse_reveal(reveal):
  parsed_values = { value: int(key) for key, value in dict(re.findall(reveal_pattern, reveal)).items()}
  return parsed_values

def parse_results(results):
  return [parse_reveal(reveal) for reveal in results.split('; ')]

def parse_line(line):
  line_match = re.match(line_pattern, line)
  return (int(line_match.group('number')), parse_results(line_match.group('results')))

def day2_1():
  with open('./day2_advent_input.txt', 'r') as input:
    parsed_input = dict([parse_line(line) for line in input])
    valid_keys = [key for key, value in parsed_input.items() if all([within_threshold(reveal) for reveal in value])]
    return sum(valid_keys)

def day2_2():
  pass
