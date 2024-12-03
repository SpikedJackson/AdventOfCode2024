import re
#part 1
with open("input3.txt") as f:
    lines = f.readlines()
pattern = r"mul\((\d+),(\d+)\)"
total = 0
matches = []
for line in lines:
    matches += re.findall(pattern,line)
for match in matches:
    total += int(match[0])*int(match[1])
print(total)

#part 2
with open("input3.txt") as f:
    line = f.read()
total = 0
matches = []

def removeDont(line):
    find = line.find("don't()")
    if (find == -1):
        return line
    else:
        return line[:find] + addDo(line[find:])
def addDo(line):
    find = line.find("do()")
    if (find == -1):
        return ""
    else:
        return removeDont(line[find:])

matches += re.findall(pattern,removeDont(line))
for match in matches:
    total += int(match[0])*int(match[1])
print(total)