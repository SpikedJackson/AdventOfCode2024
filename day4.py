with open("input4.txt") as f:
    lines = f.readlines()

# part 1
# map each letter in the word XMAS to int
map = {0:'X',1:'M',2:'A',3:'S'}
end = 3

# save the bound where the word XMAS can no longer fit
BOUND = len(lines) - 3

# given the current row, column and letter of the word XMAS,
# determine if following the direction (up,down,left,right,diagonal)
# spells the entire word.
# always start with X and recurse
def checkUp(row,column,letter):
    if letter == end:
        return True
    if lines[row-1][column] == map[letter+1]:
        return checkUp(row-1,column,letter+1)
    return False

def checkDown(row,column,letter):
    if letter == end:
        return True
    if lines[row+1][column] == map[letter+1]:
        return checkDown(row+1,column,letter+1)
    return False

def checkLeft(row,column,letter):
    if letter == end:
        return True
    if lines[row][column-1] == map[letter+1]:
        return checkLeft(row,column-1,letter+1)
    return False

def checkRight(row,column,letter):
    if letter == end:
        return True
    if lines[row][column+1] == map[letter+1]:
        return checkRight(row,column+1,letter+1)
    return False

def checkUpLeft(row,column,letter):
    if letter == end:
        return True
    if lines[row-1][column-1] == map[letter+1]:
        return checkUpLeft(row-1,column-1,letter+1)
    return False

def checkUpRight(row,column,letter):
    if letter == end:
        return True
    if lines[row-1][column+1] == map[letter+1]:
        return checkUpRight(row-1,column+1,letter+1)
    return False

def checkDownLeft(row,column,letter):
    if letter == end:
        return True
    if lines[row+1][column-1] == map[letter+1]:
        return checkDownLeft(row+1,column-1,letter+1)
    return False

def checkDownRight(row,column,letter):
    if letter == end:
        return True
    if lines[row+1][column+1] == map[letter+1]:
        return checkDownRight(row+1,column+1,letter+1)
    return False

# given a position in the grid which is the letter X
# count the number of times it spells XMAS in any direction
def checkAll(row,column):
    sum = 0
    if row > 2 and checkUp(row,column,0):
        sum+=1
    if row < BOUND and checkDown(row,column,0):
        sum+=1
    if column > 2 and checkLeft(row,column,0):
        sum+=1
    if column < BOUND and checkRight(row,column,0):
        sum+=1
    if row > 2 and column > 2 and checkUpLeft(row,column,0):
        sum+=1
    if row > 2 and column < BOUND and checkUpRight(row,column,0):
        sum+=1
    if row < BOUND and column > 2 and checkDownLeft(row,column,0):
        sum+=1
    if row < BOUND and column < BOUND and checkDownRight(row,column,0):
        sum+=1
    return sum

# sum the number of times the word XMAS appears, counting from each X
total = 0
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == 'X':
            total += checkAll(i,j)
print("Part One: {}".format(total))

# part 2
# map each letter in the word MAS to int
map = {0:'M',1:'A',2:'S'}
end = 2

# save the bound where the word MAS can not fit 
# (we start from A so we only need 1 letter gap)
BOUND = len(lines) - 1

# given a position in the grid which is the letter A
# return True if it spells MAS along its diagonals
def checkAllTwo(row,column):
    sum = 0
    if checkUpLeft(row+2,column+2,-1):
        sum+=1
    if checkUpRight(row+2,column-2,-1):
        sum+=1
    if checkDownLeft(row-2,column+2,-1):
        sum+=1
    if checkDownRight(row-2,column-2,-1):
        sum+=1
    return sum==2

# sum the number of times the word MAS appears, counting from each A
total = 0
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == 'A' and 0 < i < BOUND and 0 < j < BOUND and checkAllTwo(i,j):
            total += 1
print("Part Two: {}".format(total))
