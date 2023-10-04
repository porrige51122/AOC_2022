# Read from file "input.txt" and return a list of strings. Each string is one line from the file.
input_lines = []
with open("input.txt", "r") as file:
    for line in file:
        input_lines.append(line)

# One line should be blank, split the list into two lists at the blank line
line_index = input_lines.index("\n")
first_list = input_lines[:line_index]
second_list = input_lines[line_index + 1:]

stacks_count = 9
stacks = ["" for _ in range(stacks_count)]

# ignore the last line as it is visualisation of the stacks
for line in first_list[:-1]:
    for j in range(stacks_count):
        stacks[j] = stacks[j] + line[(j * 4) + 1]

stacks = [s.strip() for s in stacks]
# for line in stacks:
#     print(line)

def printstacks(stacks):
    for line in stacks:
        print(line)

# Part 1
# ======
# Make a copy of the stacks
print("Part 1:")
stacks_copy = stacks.copy()

# For each line in the second list, split it by spaces
# The first number is the quantity, the second number is the stack number to move
# from and the third number is the stack number to move to
for line in second_list:
    split = line.split()
    quantity = int(split[1])
    from_stack = int(split[3]) - 1
    to_stack = int(split[5]) - 1

    stacks_copy[to_stack] = stacks_copy[from_stack][0:quantity][::-1] + stacks_copy[to_stack]
    stacks_copy[from_stack] = stacks_copy[from_stack][quantity:]

# Print the stacks
for line in stacks_copy:
    print(line[0], end="")
print()

# Part 2
# ======
print("Part 2:")
stacks_copy = stacks.copy()

# For each line in the second list, split it by spaces
# The first number is the quantity, the second number is the stack number to move
# from and the third number is the stack number to move to
for line in second_list:
    split = line.split()
    quantity = int(split[1])
    from_stack = int(split[3]) - 1
    to_stack = int(split[5]) - 1

    stacks_copy[to_stack] = stacks_copy[from_stack][0:quantity] + stacks_copy[to_stack]
    stacks_copy[from_stack] = stacks_copy[from_stack][quantity:]

# Print the stacks
for line in stacks_copy:
    print(line[0], end="")
print()
