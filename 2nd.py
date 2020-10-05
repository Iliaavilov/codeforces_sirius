import sys

input = [line.strip() for line in sys.stdin]

left = int(input[0])
mid = int(input[1])
right = int(input[2])

full_cycles = min(left, right, mid // 2)
left = left - full_cycles
right = right - full_cycles
mid= mid - 2*full_cycles

full_time = full_cycles*4
if left>0:
    full_time = full_time + 1
    if mid>0:
        full_time = full_time + 1
        if right > 0:
            full_time = full_time + 1
print(full_time)