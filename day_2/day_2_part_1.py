"""
"The first column is what your opponent is going to play: 
A for Rock, B for Paper, and C for Scissors. The second column--" 

The second column, you reason, must be what you should play in response: 
X for Rock, Y for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses 
must have been carefully chosen.

The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).

"""

# Rock = A or X
# Paper = B or Y
# scissors = C or Z


def shape_score(input):
    if input == "X":
        current_shape_score = 1
    if input == "Y":
        current_shape_score = 2
    if input == "Z":
        current_shape_score = 3

    return current_shape_score


with open("input") as f:
    input = f.readlines()


winning_combos = [("A", "Y"), ("B", "Z"), ("C", "X")]
ties = [("A", "X"), ("B", "Y"), ("C", "Z")]

score = 0
for line in input:
    opponent = line[0]
    us = line[2]

    if not (opponent, us) in winning_combos:
        outcome = 0
    if (opponent, us) in winning_combos:
        outcome = 6
    if (opponent, us) in ties:
        outcome = 3

    shape = shape_score(us)

    score_this_round = shape + outcome
    score = score + score_this_round

print("total score is {}".format(score))
