import sys

input = [line.strip() for line in sys.stdin]

len_att = int(input[0])
input = [int(el) for el in input[1:]]

right = [None]*len_att
left = [None]*len_att
lenghts = [10**8]*len_att
answer = 0

for i in range(1, ((len_att // 2) + 1)):
    for t in range(i, (len_att-i+1)):
        center = input[t]
        if (type(left[t]) != int) & (left[t] != False):
            my_range_left = input[(t - i): t][::-1]
            b = -1
            for left_el in my_range_left:
                if left_el> center:
                    left[t] = False
                    break
                elif left_el<center:
                    left[t] = t + b
                    break
                b = b-1
        if (type(right[t]) != int) & (right[t] != False):
            my_range_right = input[(t+1): (t+i+1)]
            b = 1
            for right_el in my_range_right:
                if right_el>center:
                    right[t] = False
                    break
                elif right_el<center:
                    right[t] = t + b
                    break
                b = b+1
        if (type(right[t]) == int) & (type(left[t]) == int):
            lenghts[t] = right[t] - left[t]
            answer = 'aa'

if answer != 0:
    min_idx = lenghts.index(min(lenghts))

    print(left[min_idx] + 1, right[min_idx] + 1)
else:
    print(0)

