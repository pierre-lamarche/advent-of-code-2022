import re

input = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day04/input.txt"

with open(input, mode='r') as f:
    assignments = f.read().split("\n")

assignments = [re.match(r'(\d+)-(\d+),(\d+)-(\d+)', assignment) for assignment in assignments if assignment != '']
assignments = [(set(range(int(m.group(1)), int(m.group(2)) + 1)),
                set(range(int(m.group(3)), int(m.group(4)) + 1)))
               for m in assignments]

sum([1 if len(assignment[0] - assignment[1]) == 0 or len(assignment[1] - assignment[0]) == 0 else 0 for assignment in assignments])

sum([1 if len(assignment[0].intersection(assignment[1])) > 0 else 0 for assignment in assignments])