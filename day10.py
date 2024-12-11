with open("input10.txt") as f:
    lines = f.readlines()
BOUND = len(lines)-1

# part 1
def checkUp(row,column,num):
    if lines[row-1][column] == num+1:
        if num == 8:
            return {(row-1,column)}
        return checkAll(row-1,column,num+1)
    return set()

def checkDown(row,column,num):
    if lines[row+1][column] == num+1:
        if num == 8:
            return {(row+1,column)}
        return checkAll(row+1,column,num+1)
    return set()

def checkLeft(row,column,num):
    if lines[row][column-1] == num+1:
        if num == 8:
            return {(row,column-1)}
        return checkAll(row,column-1,num+1)
    return set()

def checkRight(row,column,num):
    if lines[row][column+1] == num+1:
        if num == 8:
            return {(row,column+1)}
        return checkAll(row,column+1,num+1)
    return set()

def checkAll(row,column,num):
    locations = set()
    if row > 0:
        locations |= checkUp(row,column,num)
    if row < BOUND:
        locations |= checkDown(row,column,num)
    if column > 0:
        locations |= checkLeft(row,column,num)
    if column < BOUND:
        locations |= checkRight(row,column,num)
    return locations

total = 0
for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i].strip()]
for i,line in enumerate(lines):
    for j,num in enumerate(line):
        if num == 0:
            total += len(checkAll(i,j,num))
print(total)
# part 2
def checkUpTwo(row,column,num):
    if lines[row-1][column] == num+1:
        if num == 8:
            return 1
        return checkAllTwo(row-1,column,num+1)
    return 0

def checkDownTwo(row,column,num):
    if lines[row+1][column] == num+1:
        if num == 8:
            return 1
        return checkAllTwo(row+1,column,num+1)
    return 0

def checkLeftTwo(row,column,num):
    if lines[row][column-1] == num+1:
        if num == 8:
            return 1
        return checkAllTwo(row,column-1,num+1)
    return 0

def checkRightTwo(row,column,num):
    if lines[row][column+1] == num+1:
        if num == 8:
            return 1
        return checkAllTwo(row,column+1,num+1)
    return 0

def checkAllTwo(row,column,num):
    locations = 0
    if row > 0:
        locations += checkUpTwo(row,column,num)
    if row < BOUND:
        locations += checkDownTwo(row,column,num)
    if column > 0:
        locations += checkLeftTwo(row,column,num)
    if column < BOUND:
        locations += checkRightTwo(row,column,num)
    return locations

total = 0
for i,line in enumerate(lines):
    for j,num in enumerate(line):
        if num == 0:
            total += checkAllTwo(i,j,num)
print(total)