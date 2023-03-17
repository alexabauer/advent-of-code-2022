## Part 1: In how many assignment pairs does one range fully contain the other?

# with open('./inputs/day04') as f:
#     lines = [line.strip() for line in f.readlines()] # read in input
#     containing_pairs = []
#     for line in lines:
#         r1, r2 = [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in line.split(",")] # split lines into two ranges and identify the start and end values for each range
#         if r1[0] <= r2[0] and r1[-1] >= r2[-1]:
#             containing_pairs.append(1)
#         elif r2[0] <= r1[0] and r2[-1] >= r1[-1]:
#             containing_pairs.append(1)
#     print(sum(containing_pairs))

## Part 2: In how many assignment pairs do the ranges overlap?

with open('./inputs/day04') as f:
    lines = [line.strip() for line in f.readlines()] # read in input
    overlapping_range = []
    for line in lines:
        r1, r2 = [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in line.split(",")]
        if r1[0] <= r2[0] <= r1[-1]:
            overlapping_range.append(1)
        elif r2[0] <= r1[0] <= r2[-1]:
            overlapping_range.append(1)
    print(sum(overlapping_range))