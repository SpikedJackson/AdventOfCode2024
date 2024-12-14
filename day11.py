# process input
with open("input11.txt") as f:
    line = f.read()
line = line.split(" ")
original = dict()
for stone in line:
    # each label is mapped to the number of times it appears
    original[stone] = 1

# memoized function
memo = dict()
def checkStone(stone):

    # check if result is in memo already
    if stone in memo:
        return memo[stone]
    
    stone_length = len(stone)

    # rule 1, 0 becomes 1
    if stone == "0":
        memo[stone] = ["1"]
    
    # rule 2, even number of digits is split into two stones
    elif stone_length % 2 == 0:
        stone1 = stone[:stone_length//2].lstrip("0")
        stone2 = stone[stone_length//2:].lstrip("0")
        if stone2 == '':
            stone2 = "0"
        memo[stone] = [stone1,stone2]

    # rule 3, odd number of digits is multiplied by 2024
    else:
        memo[stone] = [str(int(stone)*2024)]
    
    return memo[stone]

def observeStones(blinks):

    # make copy of dictionary so part 2 isnt messed up by part 1
    count = dict(original)

    # every blink compute the result for each label
    for blink in range(blinks):
        count2 = dict(count)
        for stone in count2:
            results = checkStone(stone)

            # use the result for as many times as that label is in the line
            for result in results:
                if result in count:
                    count[result] += count2[stone]
                else:
                    count[result] = count2[stone]
            count[stone] -= count2[stone]

            # dont store the count of any labels which have no stones
            if count[stone] == 0:
                del count[stone]
    
    # return the total number of labels
    total = 0
    for stone in count:
        total += count[stone]
    return total

print("Part One: {}".format(observeStones(25)))
print("Part Two: {}".format(observeStones(75)))