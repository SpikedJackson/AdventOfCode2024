import re
with open("input1.txt") as f:
    lines = f.readlines()

# part 1
list1 = []
list2 = []
pattern = r"(\d+)\s{3}(\d+)"

# sort the lists of numbers
for line in lines:
    list1.append(int(re.search(pattern, line).group(1)))
    list2.append(int(re.search(pattern, line).group(2)))
list1.sort()
list2.sort()

# sum the difference between the corrosponding numbers in the lists
total = 0
for i in range(len(list1)):
    total+=abs(list1[i] - list2[i])
print("Part One: {}".format(total))

# part 2
# sum the numbers in list one times the number of times they appear in list two
total = 0
for i in range(len(list1)):
    total+=list1[i]*list2.count(list1[i])
print("Part Two: {}".format(total))
