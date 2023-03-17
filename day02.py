## Part 1: What would your total score be if everything goes exactly according to your strategy guide?

# A & X: Rock (1 pt)
# B & Y: Paper (2 pt)
# C & Z: Scissors (3 pt)

# win: 6 pt
# draw: 3 pt
# loss: 0 pt

score_map = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

# with open("./inputs/day02") as f:
#     lines = f.readlines()
#     strategy_guide = []
#     for line in lines:
#         strip = line.strip()
#         value = score_map[strip]
#         strategy_guide.append(value)
#     print(sum(strategy_guide))

## Part 2: Following the Elf"s instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

# X: lose
# Y: draw
# Z: win

shape_map = { # write "old" code behind new condition, then add line to when loop to first replace new condition with old condition, then give us the value!
  "A X": "A Z",
  "A Y": "A X",
  "A Z": "A Y",
  "B X": "B X",
  "B Y": "B Y",
  "B Z": "B Z",
  "C X": "C Y",
  "C Y": "C Z",
  "C Z": "C X"
}

with open("./inputs/day02") as f:
    lines = f.readlines()
    strategy_guide = []
    strategy_guide_new = []
    for line in lines:
        strip = line.strip()
        strategy = shape_map[strip]
        strategy_guide.append(strategy)
    for row in strategy_guide:
        strip2 = row.strip()
        value = score_map[strip2]
        strategy_guide_new.append(value)
    print(sum(strategy_guide_new))


