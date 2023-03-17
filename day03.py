# ## Part 1: What is the sum of the priorities of those item types?
# # Find the item type that appears in both compartments of each rucksack.

# item_priority = { # item priority values
#   "a" : 1,
#   "b" : 2,
#   "c" : 3,
#   "d" : 4,
#   "e" : 5,
#   "f" : 6,
#   "g" : 7,
#   "h" : 8,
#   "i" : 9,
#   "j" : 10,
#   "k" : 11,
#   "l" : 12,
#   "m" : 13,
#   "n" : 14,
#   "o" : 15,
#   "p" : 16,
#   "q" : 17,
#   "r" : 18,
#   "s" : 19,
#   "t" : 20,
#   "u" : 21,
#   "v" : 22,
#   "w" : 23,
#   "x" : 24,
#   "y" : 25,
#   "z" : 26,
#   "A" : 27,
#   "B" : 28,
#   "C" : 29,
#   "D" : 30,
#   "E" : 31,
#   "F" : 32,
#   "G" : 33,
#   "H" : 34,
#   "I" : 35,
#   "J" : 36,
#   "K" : 37,
#   "L" : 38,
#   "M" : 39,
#   "N" : 40,
#   "O" : 41,
#   "P" : 42,
#   "Q" : 43,
#   "R" : 44,
#   "S" : 45,
#   "T" : 46,
#   "U" : 47,
#   "V" : 48,
#   "W" : 49,
#   "X" : 50,
#   "Y" : 51,
#   "Z" : 52  
# }

# with open('./inputs/day03') as f:
#     lines = f.readlines() # read in input

#     shared_items = [] # empty list for shared item in compartment 1 and 2
#     for line in lines: # for every backpack
#         strip = line.strip() # clean up string, then split string in half and assign to respective compartments
#         c1 = strip[:len(strip)//2] 
#         c2 = strip[len(strip)//2:]
#         for i in c1: # check every letter if present in c1 AND c2, and if so, assign to new variable
#             if i in c2:
#                 res = i
#         value = item_priority[res] # identify priority value of identified letter 
#         shared_items.append(value) # save value to list
#     print(sum(shared_items))

# ## Part 2: What is the sum of the priorities of those item types?
# # Find the item type that corresponds to the badges of each three-Elf group.

# with open('./inputs/day03') as f:
#     lines = [line.strip() for line in f.readlines()] # read in input
#     chunks = [lines[x:x+3] for x in range(0, len(lines), 3)] # group by 3
#     badge = []
#     badge_value = []
#     for chunk in chunks:
#       common = set.intersection(*map(set,chunk)) # identify common item
#       badge.append(common) 
#     badge = [item for subset in badge for item in subset] # collapse set of sets into list
#     for i in badge:
#       value = item_priority[i]
#       badge_value.append(value)
#     print(sum(badge_value))

# _Update: tried to make it neater______ TAKE 2 ________________________

def get_priority(char):           # function: get the priority value assigned to each letter
  if char.isupper():
    return ord(char) - 38     # use ord() function to get ASCII value of a character & subtract 38 so that A: 27, B: 28, ...
  else:
    return ord(char) - 96     # substract 96 for lowercase values so a:1, b:2, ...

## Part 1: What is the sum of the priorities of those item types?
# Find the item type that appears in both compartments of each rucksack.

with open('./inputs/day03') as f:
  lines = [line.strip() for line in f] # read in input
  shared_items = []
  for line in lines:
    c1 = line[:len(line)//2]
    c2 = line[len(line)//2:]
    common_set = set(c1).intersection(set(c2))    # use intersection() to find common elements insead of looping over each character
    print(common_set)
    if common_set:
      common_item = common_set.pop()
      value = get_priority(common_item)
      shared_items.append(value)
  print(sum(shared_items))

## Part 2: What is the sum of the priorities of those item types?
# Find the item type that corresponds to the badges of each three-Elf group.

  chunks = [lines[x:x+3] for x in range(0, len(lines), 3)]  # group by 3
  badge = []
  for chunk in chunks:
    common_set = set.intersection(*map(set,chunk))
    badge.append(common_set)
  badge = [item for subset in badge for item in subset]     # collapse set of sets into list
  total = 0
  for i in badge:
    value = get_priority(i)
    total += value
  print(total)