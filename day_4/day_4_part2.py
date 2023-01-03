with open("input") as f:
    input = f.readlines()

ranges_paired = []
for line in input:
    elves = line.split(",")
    elf1, elf2 = elves[0], elves[1][:-1]

    elf_ranges = []
    for assignedSec in elf1, elf2:

        # separate by the - symbol
        ranges_split = assignedSec.split("-")
        range_start = int(ranges_split[0])
        range_end = int(ranges_split[1])

        rangeBuilt = [*range(range_start, range_end + 1)]
        elf_ranges.append(rangeBuilt)

    ranges_paired.append(elf_ranges)

overlap = 0
for i, pair in enumerate(ranges_paired):
    first_range, second_range = pair[0], pair[1]
    z = [i for i in first_range if i in second_range]
    if len(z) >= 1:
        overlap += 1

print(overlap)
