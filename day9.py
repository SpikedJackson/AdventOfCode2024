with open("input9.txt") as f:
    line = f.read()

# converts disk map into list of individual blocks of files and free space
individual_blocks = []
for i,char in enumerate(line.strip()):
    if i%2 == 0:
        for j in range(0,int(char)):
            individual_blocks.append(i//2)

    else:
        for j in range(0,int(char)):
            individual_blocks.append('.')
copy = individual_blocks[:]

# part 1
# starting from the end, move files into free space at the start
for i,char in enumerate(list(reversed(copy))):
    if char != '.':

        # find first available free space
        index = individual_blocks.index('.')

        # if first space appears later than the current char, end
        if index > len(individual_blocks)-i-1:
            break

        # replace free space with char and char with free space
        individual_blocks[index] = char
        individual_blocks[-i-1] = '.'

# sum product of numbers and their index
total = 0
for i,char in enumerate(individual_blocks):
    if(char == '.'):
        break
    total+=i*int(char)
print("Part 1: {}".format(total))

# part 2

# starting from the end, attempt to move all files with same number 
# into free space at the start
copy2 = list(reversed(copy[:]))
i=0
while i < len(copy2):
    char = copy2[i]

    # if char is free space, go next
    if char == '.':
        i+=1
    else:

        # number of char we need to fit
        count_char = copy.count(char)

        # first appearance of '.'
        index = copy.index('.')

        # if char appears before first '.'
        if index > len(copy)-i-1:
            break

        # count space available
        count_space = 0
        for j, char_two in enumerate(copy[index:]):

            # if free space is now past the char
            if index+j > len(copy)-i-1:
                break

            # end of current block of free space
            if char_two != '.':
                count_space = 0
            else:
                count_space+=1
            
            # if there is enough free space in current block
            if count_char <= count_space:

                # replace free space with char and char with free space
                for k in range(count_char):
                    copy[index+j-k] = char
                    copy[-i-1-k] = '.'
                break
        
        # skip past rest of current char
        i+=count_char

# sum product of numbers and their index
total = 0
for i,char in enumerate(copy):
    if(char != '.'):
        total+=i*int(char)
print("Part 2: {}".format(total))
