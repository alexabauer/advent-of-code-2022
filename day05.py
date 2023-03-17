## Part 1: After the rearrangement procedure completes, what crate ends up on top of each stack?

# read in data for stacks
columns = {}
with open('./inputs/day05') as f:
    lines = f.readlines()
    for j, line in enumerate(lines):
        if j == 8:
            break
        for i, char in enumerate (line):
            if (char.isalpha()) == True: 
                if i not in columns:
                    columns[i] = []
                columns[i].append(char)
    for n in columns:
        columns[n].reverse() # reverse so that top block is last value in string

# assign accurate stack names to each stack 
myKeys = list(columns.keys())
myKeys.sort()
sorted_dict = {i: columns[i] for i in myKeys} 
stack = {}
for i, key in enumerate(sorted_dict, 1):
    stack[i] = columns[key]

# # move blocks
# # -> list with 3 int, where [0] is number of blocks to move, [1] starting stack, [2] target stack
# for i, line  in enumerate(lines):
#     if i >= 10:
#         num = [int(i) for i in line.split() if i.isdigit()] 
#         for x in range(num[0]): # move one stack at a time until desired number of blocks has been moved
#             wip = stack[num[2]].append(stack[num[1]].pop())

# # identify top crates for each stack
# top_crates = []
# for j in stack:
#     top_crates.append(stack[j][-1])
# print(''.join(top_crates))

## Part 2: After the rearrangement (CrateMover 9001) procedure completes, what crate ends up on top of each stack? 

# move blocks
# -> list with 3 int, where [0] is number of blocks to move, [1] starting stack, [2] target stack
for i, line  in enumerate(lines):
    if i >= 10:
        num = [int(i) for i in line.split() if i.isdigit()] 
        crates = stack[num[1]][-num[0]:]
        del stack[num[1]][-num[0]:]
        stack[num[2]] = stack[num[2]] + crates

top_crates = []
for j in stack:
    top_crates.append(stack[j][-1])
print(''.join(top_crates))