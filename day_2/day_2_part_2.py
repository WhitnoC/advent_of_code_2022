# Rock = A or X
# Paper = B or Y
# scissors = C or Z


def shape_score(input):
    if input == "rock":
        current_shape_score = 1
    if input == "paper":
        current_shape_score = 2
    if input == "scissors":
        current_shape_score = 3

    return current_shape_score


def choice_this_round(input, opponent):
    if input == "X":
        # need to lose, pick a losing result
        if opponent == "A":
            our_choice = "scissors"
        if opponent == "B":
            our_choice = "rock"
        if opponent == "C":
            our_choice = "paper"

        outcome = 0

    if input == "Y":
        # need to draw:
        if opponent == "A":
            our_choice = "rock"
        if opponent == "B":
            our_choice = "paper"
        if opponent == "C":
            our_choice = "scissors"

        outcome = 3

    if input == "Z":
        # need to win
        if opponent == "A":
            our_choice = "paper"
        if opponent == "B":
            our_choice = "scissors"
        if opponent == "C":
            our_choice = "rock"

        outcome = 6

    return our_choice, outcome


with open("input") as f:
    input = f.readlines()

"""
X means: Need to lose
Y means: need to draw
Z means: need to win
"""


score = 0
for line in input:
    opponent = line[0]
    us = line[2]

    choice, outcome = choice_this_round(us, opponent)
    shape = shape_score(choice)

    score_this_round = shape + outcome
    score = score + score_this_round

print("total score is {}".format(score))
