import re

#part 1
with open("input3.txt") as f:
    lines = f.readlines()

# use regex to find all instances of mul()
pattern = r"mul\((\d+),(\d+)\)"
matches = []
for line in lines:
    matches += re.findall(pattern,line)

# sum the results of each mul()
total = 0
for match in matches:
    total += int(match[0])*int(match[1])
print("Part One: {}".format(total))

#part 2
with open("input3.txt") as f:
    line = f.read()

# given a string line, save everything before the first dont()
def removeDont(line):
    find = line.find("don't()")
    if (find == -1):
        
        # if no dont(), return everything
        return line
    else:
        
        # return everything before dont(), recurse into searching for the next do()
        return line[:find] + addDo(line[find:])

# given a string line, delete everything before the first do()
def addDo(line):
    find = line.find("do()")
    if (find == -1):

        # if no do(), return nothing
        return ""
    else:

        # return everything after do(), recurse into searching for the next dont()
        return removeDont(line[find:])

# use regex to find all instances of mul() AFTER removing everything inside a dont()
matches = []
matches += re.findall(pattern,removeDont(line))

# sum the results of each mul()
total = 0
for match in matches:
    total += int(match[0])*int(match[1])
print("Part Two: {}".format(total))
