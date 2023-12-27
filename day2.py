from functools import reduce
import re

# { red: num1, green: num2, blue: num3 } -> True|False
def below_max(counts):
  max = {
    'red': 12,
    'green': 13,
    'blue': 14,
  }
  violators = [color for color, count in counts.items() if color in max and count > max[color]]
  return len(violators) == 0

# "num1: color1, num2: color2" -> { color1: num1, color2: num2 }
def get_colored_counts(reveal):
  numbered_color = '(\d+)\s+([^,]+)'
  return { color: int(count) for count, color in re.findall(numbered_color, reveal) }

# "num1: color1, num2: color2; num1: color1" -> [{ color1: num1, color2: num2 }, { color1: num1 }]
def get_game_results(results):
  return [get_colored_counts(reveal) for reveal in results.split('; ')]

def parse_game(line):
  game_id_with_results = '^Game\s+(?P<gameId>\d+):\s+(?P<results>.+)$'
  line_match = re.match(game_id_with_results, line)
  return (int(line_match.group('gameId')), get_game_results(line_match.group('results')))

def merge_max_counts(left, right):
  get_max_count = lambda key: max(left.get(key, 0), right.get(key, 0))
  return { key: get_max_count(key) for key in set(left) | set(right) }

def get_power(counts):
  return reduce(lambda x,y: x * y, [count for _, count in counts.items()], 1)

def day2_1():
  with open('./day2_advent_input.txt', 'r') as input:
    games = [parse_game(game_line) for game_line in input]
    game_ids = [gameId for gameId, results in games if all([below_max(counts) for counts in results])]
    return sum(game_ids)

def day2_2():
  with open('./day2_advent_input.txt', 'r') as input:
    games = [parse_game(game_line) for game_line in input]
    max_counts = [get_power(reduce(merge_max_counts, results, {})) for _, results in games]
    return sum(max_counts)
