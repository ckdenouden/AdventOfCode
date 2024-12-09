import re
from math import prod

rgb = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
games = set()
impossible_games = set()
with open("02.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n").split(":")
        game_idx = re.sub(r"\D", "", line[0])
        games.add(int(game_idx))
        game_sets = line[1].split(";")

        for game_set in game_sets:
            subset = game_set.split(", ")
            for color in subset:
                v, k = color.strip().split(" ")
                if int(v) > rgb[k]:
                    impossible_games.add(int(game_idx))
possible_games = games - impossible_games
print(sum(possible_games))

game_products = []
with open("02.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n").split(":")
        rgb = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        game_idx = re.sub(r"\D", "", line[0])
        games.add(int(game_idx))
        game_sets = line[1].split(";")
        for game_set in game_sets:
            subset = game_set.split(", ")
            for color in subset:
                v, k = color.strip().split(" ")
                if int(v) > rgb[k]:
                    rgb[k] = int(v)
        game_products.append(prod(rgb.values()))
print(sum(game_products))
