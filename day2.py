#part 1
with open("input2.txt") as f:
    lines = f.readlines()

def checkLine(line, element=-1):
    li_copy = line[:]
    if element != -1:
        li_copy.pop(element)
    #print("NEW SIZE: " + str(len(li_copy)))
    checkLess = False
    checkMore = False
    if li_copy[0] < li_copy[1]:
        checkMore = True
    elif li_copy[0] > li_copy[1]:
        checkLess = True
    else:
        return False
    for level in range(1,len(li_copy)):
        if checkMore and (li_copy[level] - li_copy[level-1] < 1 or li_copy[level] - li_copy[level-1] > 3):
            return False
        if checkLess and (li_copy[level-1] - li_copy[level] < 1 or li_copy[level-1] - li_copy[level] > 3):
            return False
    return True

def checkAll(line):
    for i in range(0,len(line)):
        if(checkLine(line,i)):
            return True
    return False

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

total = 0
for line in lines:
    line = line.split(" ")
    line = list(map(int, line))
    if(checkLine(line)):
        total+=1
print("total part 1")
print(total)

total = 0
for line in lines:
    line = line.split(" ")
    line = list(map(int, line))
    #print("ORIGINAL SIZE: " + str(len(line)))
    if(checkLinePartTwo(line)):
        total+=1
print("total part 2")
print(total)