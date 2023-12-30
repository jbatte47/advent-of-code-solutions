import re

def day4_1() -> int:
  def get_points(card: str) -> int:
    draw_pile, winner_pile = re.match('Card\s+\d+:([^\|]+)\|(.+)', card).groups()
    winners = re.findall('\d+', winner_pile)
    winning_count = sum([winners.count(draw) for draw in re.findall('\d+', draw_pile)])
    return 2 ** (winning_count - 1) if winning_count > 0 else 0

  with open('./day4_advent_input.txt', 'r') as input:
    return sum([get_points(card) for card in input])

def day4_2():
  def get_winning_count(card):
    draw_pile, winner_pile = re.match('Card\s+\d+:([^\|]+)\|(.+)', card).groups()
    winners = re.findall('\d+', winner_pile)
    winning_count = sum([winners.count(draw) for draw in re.findall('\d+', draw_pile)])
    return winning_count

  lines = list(open('./day4_advent_input.txt'))
  card_values = [0] * len(lines)

  for line_num in range(len(lines) - 1, -1, -1):
    win_count = min(get_winning_count(lines[line_num]), len(lines) - (line_num + 1))
    card_values[line_num] = 1 + sum([card_values[x] for x in range(line_num + win_count, line_num, -1)])

  return sum(card_values)
