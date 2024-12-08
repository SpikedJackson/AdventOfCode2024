with open("input7.txt") as f:
    lines = f.readlines()

# part 1
# given an answer and a list of numbers, add or multiply the first two numbers of the list
# then recurse using the result as the new first number in the list
# once there are only two numbers left, return true if their sum or product equals the answer
def checkAll(answer,numbers):
    if len(numbers) == 2:
        return (answer==numbers[0]+numbers[1]) or (answer==numbers[0]*numbers[1])
    return (checkAll(answer,[numbers[0]+numbers[1]]+numbers[2:])) or (checkAll(answer,[numbers[0]*numbers[1]]+numbers[2:]))

# part 2
# same as part 1 except you may concatenate the first two numbers
def checkAllTwo(answer,numbers):
    if len(numbers) == 2:
        return (answer==numbers[0]+numbers[1]) or (answer==numbers[0]*numbers[1]) or (answer==int(str(numbers[0])+str(numbers[1])))
    return (checkAllTwo(answer,[numbers[0]+numbers[1]]+numbers[2:])) or (checkAllTwo(answer,[numbers[0]*numbers[1]]+numbers[2:])) or (checkAllTwo(answer,[int(str(numbers[0])+str(numbers[1]))]+numbers[2:]))

# sum the number of lines which the list of numbers may equal their answer
total = 0
totalTwo = 0
for line in lines:
    answer = int(line.split(": ")[0])
    numbers = [int(x) for x in line.split(" ")[1:]]
    if checkAll(answer,numbers):
        total+=answer
    if checkAllTwo(answer,numbers):
        totalTwo+=answer
print("Part One: {}".format(total))
print("Part Two: {}".format(totalTwo))