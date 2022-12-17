## Part 1: Find the Elf with carrying the most Calories total. How many Calories is he carrying?

with open('./inputs/day01') as f:
    # lines = f.readlines()
    # new_lines = []
    # for line in lines:
    #     new_lines.append(line.strip())
    # print(new_lines)

    elf_pop = [] # list containing all elves
    elf_inv = [] # list of an elf's inventory
    for line in f.readlines(): #  read all lines in the .txt file as a string, and do the following
        if line != '\n': # if the line isn't a break,
            elf_inv.append(int(line.strip())) #  remove the break ('\n') from string & write content of line into elf list as integer
        else: # if line is break (i.e. separator of elves' inventories)
            elf_pop.append(sum(elf_inv)) # write sum of all carlories an elf is carring into the elf population list
            elf_inv = [] # overwrite with empty list to 'reset' the inventory for next elf
    elf_pop.append(sum(elf_inv)) # add last elf's total calories to the population (NOT a pretty solution!)

print("Accorind to the list, the Elf carring the most Calories is Elf #" + str(elf_pop.index(max(elf_pop))) + ". They are carrying a total of " + str(max(elf_pop)) + " Calories.")

# print(max(elf_pop))
# print(elf_pop.index(max(elf_pop)))

## Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

top_elves = 3
elf_pop.sort(reverse=True)

print("The top 3 Elves are carring a total of " + str(sum(elf_pop[0:top_elves])) + " Carlories.")