# Open the file in read mode
with open("AdventDay2Puzzle.txt") as f:
    data = f.read().splitlines()

import re

def Convert(lst):
	res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::2])
	return dict(res_dct)

#def key_value(dict, search_key):
    #for key, value in dict.items():
        #if key == search_key:
            #return value

blue_cap = 14
red_cap = 12
green_cap = 13

cube_max = {'blue': 14, 'red': 12, 'green': 13}
games_list = []
game_dicts = []

# Iterate over the lines of the file
for line in data:
    game = line.replace("Game ","").replace(":","").replace(";","").replace(",","").split()
    game.insert(0, "Game")
    # flip values to turn into dictionary
    for i in range(3, len(game), 2):
        game[i], game[i-1] = int(game[i-1]), game[i]
    game[1] = int(game[1])
    games_list.append(game)
print(games_list)
for game in games_list:
    cube_dict = {}
    blue_max = 0
    red_max = 0
    green_max = 0
    print(game)
    possible = []
    for a, b in zip(*[iter(game)] * 2):
        if a == 'red' and b > red_max:
            red_max = b
            continue
        elif a == 'green' and b > green_max:
            green_max = b
            continue
        elif a == 'blue' and b >  blue_max:
            blue_max = b
            continue
        elif a == 'Game':
            game_number = b
            continue
        else:
            continue
    cube_dict.update({"Game":game_number,"red": red_max,"green": green_max,"blue":blue_max,"res": red_max*blue_max*green_max})
    game_dicts.append(cube_dict)
print(game_dicts)
import operator
res = sum(map(operator.itemgetter('res'), game_dicts))
print(res)