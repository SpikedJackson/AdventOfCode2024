with open("input2.txt") as f:
    lines = f.readlines()

# part 1
# given a line and optionally a number to remove from the line,
# return true if numbers are all increasing or all decreasing
# and if adjacent number differ by at least one and at most three
# else return false
def checkLine(line, element=-1):
    
    # optionally, remove the number at index element
    li_copy = line[:]
    if element != -1:
        li_copy.pop(element)

    # determine if numbers are increasing or decreasing
    checkLess = False
    checkMore = False
    if li_copy[0] < li_copy[1]:
        checkMore = True
    elif li_copy[0] > li_copy[1]:
        checkLess = True
    else:
        return False

    # for every number, check if it breaks the rules
    for level in range(1,len(li_copy)):
        if checkMore and (li_copy[level] - li_copy[level-1] < 1 or li_copy[level] - li_copy[level-1] > 3):
            return False
        if checkLess and (li_copy[level-1] - li_copy[level] < 1 or li_copy[level-1] - li_copy[level] > 3):
            return False
    return True

# given a line, check if removing any number makes it follow the rules
def checkAll(line):
    for i in range(0,len(line)):
        if(checkLine(line,i)):
            return True
    return False

# same as part one, but if the line doesnt follow the rules proceed to checkAll()
def checkLinePartTwo(line):
    checkLess = False
    checkMore = False
    if line[0] < line[1]:
        checkMore = True
    elif line[0] > line[1]:
        checkLess = True
    else:
        return checkLine(line,0)
    for level in range(1,len(line)):
        if checkMore and (line[level] - line[level-1] < 1 or line[level] - line[level-1] > 3):
            return checkAll(line)
        if checkLess and (line[level-1] - line[level] < 1 or line[level-1] - line[level] > 3):
            return checkAll(line)
    return True

# sum all the lines which follow the rules
total = 0
for line in lines:
    line = line.split(" ")
    line = list(map(int, line))
    if(checkLine(line)):
        total+=1
print("Part One: {}".format(total))

# sum all the lines which follow the rules or if you can remove a number
total = 0
for line in lines:
    line = line.split(" ")
    line = list(map(int, line))
    if(checkLinePartTwo(line)):
        total+=1
print("Part Two: {}".format(total))
