with open("input6.txt") as f:
    lines = f.readlines()
bound_down = len(lines) - 1
bound_right = len(lines[0]) - 2

# part 1

def begin_part_one(direction, row, column):
    while (direction != "end"):
        visited.add((row,column))
        if direction == "up":
            direction,row,column = up(row,column)
        elif direction == "down":
            direction,row,column = down(row,column)
        elif direction == "right":
            direction,row,column = right(row,column)
        elif direction == "left":
            direction,row,column = left(row,column)

def up(row,column):
    if row == 0:
        return "end", row, column
    if lines[row-1][column] == '#':
        return "right", row, column
    else:
        return "up", row-1, column
def down(row,column):
    if row == bound_down:
        return "end", row, column
    if lines[row+1][column] == '#':
        return "left", row, column
    else:
        return "down", row+1, column
def right(row,column):
    if column == bound_right:
        return "end", row, column
    if lines[row][column+1] == '#':
        return "down", row, column
    else:
        return "right", row, column+1
def left(row,column):
    if column == 0:
        return "end", row, column
    if lines[row][column-1] == '#':
        return "up", row, column
    else:
        return "left", row, column-1

for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == '^':
            start = (i,j)
            visited = {(i,j)}
            begin_part_one("up",i,j)

print("Part 1: {}".format(len(visited)))

# part 2

def begin_part_two(direction, row, column):
    while (direction != "end"):
        visited.add((row,column,direction))
        if direction == "up":
            direction,row,column = up(row,column)
        elif direction == "down":
            direction,row,column = down(row,column)
        elif direction == "right":
            direction,row,column = right(row,column)
        elif direction == "left":
            direction,row,column = left(row,column)
        if (row,column,direction) in visited:
            return True
    return False

total = 0
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == '.':
            lines[i] = lines[i][:j] + '#' + lines[i][j+1:]
            visited = {(start[0],start[1],"up")}
            if begin_part_two("up",start[0],start[1]):
                total+=1
            lines[i] = lines[i][:j] + '.' + lines[i][j+1:]

print("Part 2: {}".format(total))