# process input
with open("input12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

BOUND_RIGHT = len(lines[0])-1
BOUND_DOWN = len(lines)-1

# part 1: given the current plot, the plots in its region so far, and the regions current perimeter,
# check if its neighbours should belong to the same region, and recurse into them
# add 1 to perimeter for every neighbour not belonging to the region
def findRegion(row,column,plots,perimeter):
    # check up
    if row > 0 and lines[row][column] == lines[row-1][column]:
        if (row-1,column) not in plots:
            plots.add((row-1,column))
            plots,perimeter = findRegion(row-1,column,plots,perimeter)
    else:
        perimeter+=1
    
    # check down
    if row < BOUND_DOWN and lines[row][column] == lines[row+1][column]:
        if (row+1,column) not in plots:
            plots.add((row+1,column))
            plots,perimeter = findRegion(row+1,column,plots,perimeter)
    else:
        perimeter+=1
    
    # check left
    if column > 0 and lines[row][column] == lines[row][column-1]:
        if (row,column-1) not in plots:
            plots.add((row,column-1))
            plots,perimeter = findRegion(row,column-1,plots,perimeter)
    else:
        perimeter+=1
    
    # check right
    if column < BOUND_RIGHT and lines[row][column] == lines[row][column+1]:
        if (row,column+1) not in plots:
            plots.add((row,column+1))
            plots,perimeter = findRegion(row,column+1,plots,perimeter)
    else:
        perimeter+=1
    return plots,perimeter

# given a plot, return its neighbours
def neighbours(plot):
    return [(plot[0]-1,plot[1]), (plot[0]+1,plot[1]), (plot[0],plot[1]-1), (plot[0],plot[1]+1)]

# part 2: given a region, compute its number of duplicate sides
def dupeSides(plots):
    dupes = 0
    for plot in plots:
        for neighbour in neighbours(plot):
            if neighbour in plots:
                for i in range(4):

                    # if the plot's neighbour is in the region and they both added a side to the perimeter from the same direction
                    if neighbours(neighbour)[i] not in plots and neighbours(plot)[i] not in plots:
                        dupes+=1
    
    # since this double counted each duplicate
    return dupes//2

counted = set()
total = 0
total2 = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):

        # for each plot not already counted as part of another region
        if (i,j) not in counted:

            # begin a new region with this plot, perimeter 0
            plots = {(i,j)}
            perimeter = 0
            sides = 0

            # compute the plots belonging to this region and its perimeter
            plots,perimeter = findRegion(i,j,plots,perimeter)

            # compute the number of sides of a plot
            sides = perimeter - dupeSides(plots)

            # add plots from this region to our count
            counted = counted | plots

            # compute total
            area = len(plots)
            total += area * perimeter
            total2 += area * sides
print("Part 1: {}".format(total))
print("Part 2: {}".format(total2))