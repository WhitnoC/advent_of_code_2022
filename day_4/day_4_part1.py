with open("input") as f:
    input = f.readlines()

matching_assignments = 0
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

    z = [i for i in elf_ranges[0] if i in elf_ranges[1]]
    if len(z) == len(elf_ranges[0]):
        matching_assignments = matching_assignments + 1
    elif len(z) == len(elf_ranges[1]):
        matching_assignments = matching_assignments + 1

print(matching_assignments)
