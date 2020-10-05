import sys

input = [line.strip() for line in sys.stdin]

answer = int(input[0])+int(input[1])
if (answer < 0) & (int(input[0]) < 0):
    print(answer)
elif (answer > 0) & (int(input[0]) < 0):
    print(answer+1)
elif (answer > 0) & (int(input[0]) > 0):
    print(answer)
elif (answer < 0) & (int(input[0]) > 0):
    print(answer-1)