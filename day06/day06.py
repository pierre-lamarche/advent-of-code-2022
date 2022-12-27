input = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day06/input.txt"

with open(input, mode='r') as f:
    datastream = f.read()

stop = False
i = 4

while not stop and i < len(datastream):
    if len(set(datastream[i-4:i])) < 4:
        i += 1
    else:
        stop = True

stop = False
i = 14

while not stop and i < len(datastream):
    if len(set(datastream[i-14:i])) < 14:
        i += 1
    else:
        stop = True