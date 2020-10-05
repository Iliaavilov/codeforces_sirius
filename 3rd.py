import sys

input = [line.strip() for line in sys.stdin]

max_width = int(input[0])
len_fence = int(input[1])
input = input[2:]

i = 0
num = 0
while len(input) > 0:
    if input[i] == '0':
        input.pop(0)
    else:
        if len(input)>= max_width:
            for t in range(0, max_width):
                input.pop(0)
            num+=1
        else:
            num+=1
            break
print(num)