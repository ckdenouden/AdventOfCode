translate_move = {"X": "A", "Y": "B", "Z": "C"}
base_scores = {"A": 1, "B": 2, "C": 3}
round_scores = {"AA": [3, 3], "AB": [0, 6], "AC": [6, 0],
                "BA": [6, 0], "BB": [3, 3], "BC": [0, 6],
                "CA": [0, 6], "CB": [6, 0], "CC": [3, 3]}
total_score_opp, total_score_you = 0, 0
with open("day02.txt", "r") as f:
    for line in f.readlines():
        game = line.replace("\n", "")
        opp, you = game.split(" ")
        you = translate_move[you]

        base_score_opp = base_scores[opp]
        base_score_you = base_scores[you]
        round_score_opp, round_score_you = round_scores[opp+you]
        total_score_opp += base_score_opp + round_score_opp
        total_score_you += base_score_you + round_score_you
print("1. Total score opponent:", total_score_opp)
print("1. Total score you:", total_score_you)


lose_move = {"A": "C", "B": "A", "C": "B"}
best_move = {"A": "B", "B": "C", "C": "A"}


total_score_opp, total_score_you = 0, 0
with open("day02.txt", "r") as f:
    for line in f.readlines():
        game = line.replace("\n", "")
        opp, outcome = game.split(" ")
        if outcome == "X":
            you = lose_move[opp]
        elif outcome == "Y":
            you = opp
        elif outcome == "Z":
            you = best_move[opp]

        base_score_opp = base_scores[opp]
        base_score_you = base_scores[you]
        round_score_opp, round_score_you = round_scores[opp+you]
        total_score_opp += base_score_opp + round_score_opp
        total_score_you += base_score_you + round_score_you
print("2. Total score opponent:", total_score_opp)
print("2. Total score you:", total_score_you)