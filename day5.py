with open("input5.txt") as f:
    lines = f.readlines()

# find index where rules end and pages to produce begin
seperate = lines.index("\n")

# create dictionary which maps page to array of pages that must come after it
befores = {}
for line in lines[:seperate]:
    line = [ int (x) for x in line.split("|") ]
    if line[0] in befores.keys():
        befores[line[0]].append(line[1])
    else:
        befores[line[0]] = [line[1]]

# determine if pages to produce follow ordering rules, takes in line reversed
def checkAll(line):
    for i,num in enumerate(line):

        # if we reach the last element, then complete
        if i == len(line)-1:
            return True
        
        # for each element check if all elements before it are not supposed to be after it (but reversed)
        if num in befores.keys():
            for elm in line[i+1:]:
                if elm in befores[num]:
                    return False

#part 1
total = 0
for line in lines[seperate+1:]:
    line = [ int (x) for x in line.split(",")]
    middle = line[len(line) // 2]

    # if pages to produce follow ordering rules, add middle to total
    if (checkAll(list(reversed(line)))):
        total+=middle
print("Part 1: {}".format(total))

# fixes the ordering of pages to produce to follow ordering rules
def fixLine(line,before=-1,after=-1):

    # if defined, swap elements in wrong order
    if before != -1:
        temp = line[before]
        line[before] = line[after]
        line[after] = temp

    for i,num in enumerate(line):

        # if we reach the last element, then complete (return middle)
        if i == len(line)-1:
            return line[len(line) // 2]
        
        # for each element check if all elements before it are not supposed to be after it (but reversed)
        if num in befores.keys():
            for elm in line[i+1:]:

                # if out of order, try again with the elements swapped
                if elm in befores[num]:
                    return fixLine(line,i,line.index(elm))

#part 2
total = 0
for line in lines[seperate+1:]:
    line = [ int (x) for x in line.split(",")]

    # if pages to produce don't follow ordering rules, fix and add middle to total
    if (not checkAll(list(reversed(line)))):
        total+=fixLine(list(reversed(line)))
print("Part 2: {}".format(total))