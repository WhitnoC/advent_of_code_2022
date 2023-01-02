with open("input") as f:
    lines = f.readlines()

food_items_per_elf = []
number_elves = 0
previous_elf = 0
line_breaks = []
for i, line in enumerate(lines):
    if line == "\n":
        line_breaks.append(i)
        number_elves += 1
        # take a slice from the index point of where the elf exists, to where the previous elf was.
        elf_food = lines[previous_elf:i]
        previous_elf = i
        food_items_per_elf.append(elf_food)


calorie_counts = []
for x, items in enumerate(food_items_per_elf):
    calories = 0

    for item in items:
        if not item.startswith("\n"):
            calories_this_item = int(item[:-1])
            calories = calories + calories_this_item

    calorie_counts.append(calories)


print(len(calorie_counts))

print(
    "elf {} has the most calories, with {} calories stored.".format(
        calorie_counts.index(max(calorie_counts)), max(calorie_counts)
    )
)

# Sort the list in ascending order so we can find the three largest elements.
sorted_list = sorted(calorie_counts)

elf_1, elf_2, elf_3 = sorted_list[-1], sorted_list[-2], sorted_list[-3]

print(
    "the three largest calorie counts are {}, {} and {}.".format(
        sorted_list[-1], sorted_list[-2], sorted_list[-3]
    )
)

print("sum of calories for these three elves, is {}".format(elf_1 + elf_2 + elf_3))
