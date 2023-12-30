import re

def get_winning_count(card: str) -> int:
  draw_pile, winner_pile = re.match('Card\s+\d+:([^\|]+)\|(.+)', card).groups()
  winners = re.findall('\d+', winner_pile)
  return sum([winners.count(draw) for draw in re.findall('\d+', draw_pile)])

def day4_1() -> int:
  def get_points(card: str) -> int:
    winning_count = get_winning_count(card)
    return 2 ** (winning_count - 1) if winning_count > 0 else 0

  return sum([get_points(card) for card in list(open('./day4_advent_input.txt'))])

def day4_2() -> int:
  lines = list(open('./day4_advent_input.txt'))
  card_values = [0] * len(lines)

  for line_num in range(len(lines) - 1, -1, -1):
    extra_cards = min(get_winning_count(lines[line_num]), len(lines) - (line_num + 1))
    card_values[line_num] = 1 + sum([card_values[x] for x in range(line_num + extra_cards, line_num, -1)])

  return sum(card_values)
