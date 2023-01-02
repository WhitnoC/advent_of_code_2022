"""
Not completed yet.
"""

import string

lowercase_items = string.ascii_lowercase
uppercase_items = string.ascii_uppercase

lowercase_score = [*range(1, 27)]
uppercase_score = [*range(27, 53)]

with open("input") as f:
    input = f.readlines()


elf_group_max = len(input) // 3
elf_groups = list(zip(*(iter(input),) * 3))


badges = []
scores = []
total_score = 0
for group in elf_groups:
    group_formatted = []
    for line in group:
        group_formatted.append(str(line[:-1]))

    common = set.intersection(*map(set, group_formatted)).pop()

    if common in lowercase_items:
        score_for_item = lowercase_score[lowercase_items.index(common)]

    if common in uppercase_items:
        score_for_item = uppercase_score[uppercase_items.index(common)]

    scores.append(score_for_item)
    total_score = total_score + score_for_item

print(total_score)
