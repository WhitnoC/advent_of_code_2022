with open("input", "r") as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

datastream = lines

# part 1
characters_used = []
markers = []
character_min = 3
for i, char in enumerate(datastream[0]):
    if i > character_min:
        # print(characters_used)
        if len(set(characters_used)) > 3:
            markers.append(i)

        characters_used.pop(0)

    characters_used.append(char)

print("start of packet marker detected at {}".format(markers[0]))

# part 2
characters_used = []
markers = []
character_min = 14
for i, char in enumerate(datastream[0]):
    if i >= character_min:
        # print(characters_used)
        if len(set(characters_used)) >= character_min:
            markers.append(i)

        characters_used.pop(0)

    characters_used.append(char)

print("start of packet marker detected at {}".format(markers[0]))
