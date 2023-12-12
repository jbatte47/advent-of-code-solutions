import re

def parse_and_add_first_last_digits(text):
  digits = re.findall("\d{1}", text)
  if len(digits) == 1:
    first = last = digits[0]
  else:
    first, *_, last = digits
  return int(first + last)

number_words = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}
pattern = f"{'|'.join(sorted(number_words.keys(), key=lambda w: (-len(w), w)))}|\d{{1}}"

def eval_match(match):
  if match is None:
    return None
  
  match_text = match.group()
  if match_text.isdigit():
      return match_text
  else:
      return number_words[match_text.lower()]

def get_left_number(text):
  return eval_match(re.search(pattern, text))

def get_right_number(text):
  for i in range(len(text)):
    right_side = text[-(i+1):]
    match = eval_match(re.match(pattern, right_side))
    if match is not None:
      return match
  return None

def parse_and_add_first_last_digits_v2(text):
  left = get_left_number(text)
  right = get_right_number(text) or left
  return int(left + right)

def day1_1():
  with open('./day1_advent_input.txt', 'r') as input:
    return sum(parse_and_add_first_last_digits(line) for line in input)
  
def day1_2():
  with open('./day1_advent_input.txt', 'r') as input:
    return sum(parse_and_add_first_last_digits_v2(line) for line in input)
