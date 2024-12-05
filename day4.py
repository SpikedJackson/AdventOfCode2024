#part 1
with open("input4.txt") as f:
    lines = f.readlines()
total = 0
map = {0:'X',1:'M',2:'A',3:'S'}
BOUND = len(lines) - 3

def checkUp(row,column,letter):
    if letter == 3:
        return True
    if lines[row-1][column] == map[letter+1]:
        return checkUp(row-1,column,letter+1)
    return False

def checkDown(row,column,letter):
    if letter == 3:
        return True
    if lines[row+1][column] == map[letter+1]:
        return checkDown(row+1,column,letter+1)
    return False

def checkLeft(row,column,letter):
    if letter == 3:
        return True
    if lines[row][column-1] == map[letter+1]:
        return checkLeft(row,column-1,letter+1)
    return False

def checkRight(row,column,letter):
    if letter == 3:
        return True
    if lines[row][column+1] == map[letter+1]:
        return checkRight(row,column+1,letter+1)
    return False

def checkUpLeft(row,column,letter):
    if letter == 3:
        return True
    if lines[row-1][column-1] == map[letter+1]:
        return checkUpLeft(row-1,column-1,letter+1)
    return False

def checkUpRight(row,column,letter):
    if letter == 3:
        return True
    if lines[row-1][column+1] == map[letter+1]:
        return checkUpRight(row-1,column+1,letter+1)
    return False

def checkDownLeft(row,column,letter):
    if letter == 3:
        return True
    if lines[row+1][column-1] == map[letter+1]:
        return checkDownLeft(row+1,column-1,letter+1)
    return False

def checkDownRight(row,column,letter):
    if letter == 3:
        return True
    if lines[row+1][column+1] == map[letter+1]:
        return checkDownRight(row+1,column+1,letter+1)
    return False

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

for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == 'X':
            total += checkAll(i,j)
print(total)

#part 2
with open("input4.txt") as f:
    lines = f.readlines()
total = 0
map = {0:'M',1:'A',2:'S'}
BOUND = len(lines) - 1

def checkUpLeft2(row,column,letter):
    if letter == 2:
        return True
    if lines[row-1][column-1] == map[letter+1]:
        return checkUpLeft2(row-1,column-1,letter+1)
    return False

def checkUpRight2(row,column,letter):
    if letter == 2:
        return True
    if lines[row-1][column+1] == map[letter+1]:
        return checkUpRight2(row-1,column+1,letter+1)
    return False

def checkDownLeft2(row,column,letter):
    if letter == 2:
        return True
    if lines[row+1][column-1] == map[letter+1]:
        return checkDownLeft2(row+1,column-1,letter+1)
    return False

def checkDownRight2(row,column,letter):
    if letter == 2:
        return True
    if lines[row+1][column+1] == map[letter+1]:
        return checkDownRight2(row+1,column+1,letter+1)
    return False

def checkAll(row,column):
    sum = 0
    if checkUpLeft2(row+2,column+2,-1):
        sum+=1
    if checkUpRight2(row+2,column-2,-1):
        sum+=1
    if checkDownLeft2(row-2,column+2,-1):
        sum+=1
    if checkDownRight2(row-2,column-2,-1):
        sum+=1
    return sum==2

for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == 'A' and 0 < i < BOUND and 0 < j < BOUND and checkAll(i,j):
            total += 1
print(total)