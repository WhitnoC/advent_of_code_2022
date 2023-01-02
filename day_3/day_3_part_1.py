import string

lowercase_items = string.ascii_lowercase
uppercase_items = string.ascii_uppercase

lowercase_score = [*range(1, 27)]
uppercase_score = [*range(27, 53)]

with open("input") as f:
    input = f.readlines()

matches = []
for line in input:

    total_size = len(line)
    component_split_index = total_size // 2

    compartment_1 = line[0:component_split_index]
    compartment_2 = line[component_split_index : len(line)]

    matching_items = []
    for item_1 in compartment_1:
        for item_2 in compartment_2:
            if item_1 == item_2:
                matching_items.append(item_1)

    matching_item = set(matching_items).pop()
    matches.append(matching_item)

score = 0
for item in matches:

    if item in lowercase_items:
        score_for_item = lowercase_score[lowercase_items.index(item)]

    if item in uppercase_items:
        score_for_item = uppercase_score[uppercase_items.index(item)]

    score = score + score_for_item


print(score)
