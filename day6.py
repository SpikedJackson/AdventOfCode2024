with open("input6.txt") as f:
    lines = f.readlines()

# save the bounds of the grid
bound_down = len(lines) - 1
bound_right = len(lines[0]) - 2

# part 1
# given a starting direction and position,
# move the guard in that direction, until he leaves the grid
# save each position they visited to a SET
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

# given a position and direction, move in that direction
# or turn 90 degrees if facing a '#'
# or end if they're going to move out of bounds
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

# find starting position and create set to track visited places
# then call begin function with starting position and direction
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == '^':
            start = (i,j)
            visited = {(i,j)}
            begin_part_one("up",i,j)

# sum unique places visited
print("Part 1: {}".format(len(visited)))

# part 2
# given a starting direction and position,
# move the guard in that direction and return false when he leaves the grid
# OR return true if he is in a loop (ie he's repeating a position with the same direction)
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

# sum the total number of locations for which adding a '#' creates a loop
# use starting position from part 1
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
