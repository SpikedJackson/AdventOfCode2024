with open("input8.txt") as f:
    lines = f.readlines()
lines = [list(line.rstrip()) for line in lines]

# create dictionary of frequencies and their locations
dict = {}
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char != '.':
            if char in dict.keys():
                dict[char].append((i,j))
            else:
                dict[char] = [(i,j)]

# part 1
# set of unique locations which contain an antinode
loc = set()

# for each frequency loop through every pair of locations
for key, value in dict.items():
    for i,coord1 in enumerate(value):
        for coord2 in value[i+1:]:

            # if adding the difference of the locations stays within bounds, then antinode exists there
            if 0 <= coord1[0] + coord1[0] - coord2[0] < len(lines) and 0 <= coord1[1] + coord1[1] - coord2[1] < len(lines[0]):
                loc.add((coord1[0] + coord1[0] - coord2[0],coord1[1] + coord1[1] - coord2[1]))
            if 0 <= coord2[0] + coord2[0] - coord1[0] < len(lines) and 0 <= coord2[1] + coord2[1] - coord1[1] < len(lines[0]):
                loc.add((coord2[0] + coord2[0] - coord1[0],coord2[1] + coord2[1] - coord1[1]))
print("Part One: {}".format(len(loc)))


# part 2
# set of unique locations which contain an antinode
loc = set()

# for each frequency loop through every pair of locations
for key, value in dict.items():
    for i,coord1 in enumerate(value):
        for coord2 in value[i+1:]:
            # while still in bounds, keep adding the distance
            i = 0
            while(0 <= coord1[0] + i*(coord1[0] - coord2[0]) < len(lines) and 0 <= coord1[1] + i*(coord1[1] - coord2[1]) < len(lines[0])):
                loc.add((coord1[0] + i*(coord1[0] - coord2[0]),coord1[1] + i*(coord1[1] - coord2[1])))
                i+=1
            i = 0
            while(0 <= coord2[0] + i*(coord2[0] - coord1[0]) < len(lines) and 0 <= coord2[1] + i*(coord2[1] - coord1[1]) < len(lines[0])):
                loc.add((coord2[0] + i*(coord2[0] - coord1[0]),coord2[1] + i*(coord2[1] - coord1[1])))
                i+=1
print("Part Two: {}".format(len(loc)))

# visualization
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == '.' and (i,j) in loc:
            lines[i][j] = '#'
for line in lines:
    print(''.join(line))