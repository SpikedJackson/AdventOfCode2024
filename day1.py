import re
#part 1
with open("input1.txt") as f:
    lines = f.readlines()
list1 = []
list2 = []
pattern = r"(\d+)\s{3}(\d+)"
for line in lines:
    list1.append(int(re.search(pattern, line).group(1)))
    list2.append(int(re.search(pattern, line).group(2)))
list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total+=abs(list1[i] - list2[i])
print(total)
#part 2
total = 0
for i in range(len(list1)):
    total+=list1[i]*list2.count(list1[i])
print(total)