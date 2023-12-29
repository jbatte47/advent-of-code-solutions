import re

def day4_1():
  def get_points(card):
    draw_pile, winner_pile = re.match('Card\s+\d+:([^\|]+)\|(.+)', card).groups()
    winners = re.findall('\d+', winner_pile)
    winning_count = sum([winners.count(draw) for draw in re.findall('\d+', draw_pile)])
    return 2 ** (winning_count - 1) if winning_count > 0 else 0

  with open('./day4_advent_input.txt', 'r') as input:
    return sum([get_points(card) for card in input])

def day4_2():
  pass
