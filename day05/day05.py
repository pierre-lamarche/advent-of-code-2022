import re

input = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day05/input.txt"

with open(input, mode="r") as f:
    crates_and_moves = f.read().split('\n')

moves = [re.match(r'move (\d+) from (\d+) to (\d+)', move) for move in crates_and_moves if re.match(r'move (\d+) from (\d+) to (\d+)', move)]
moves = [{'number': int(move.group(1)), 'origin': move.group(2), 'destination': move.group(3)} for move in moves]

line_positions = [(line,i) for i, line in enumerate(crates_and_moves) if re.match(r'^\s+1', line)][0]
crates = {str(i): [line[line_positions[0].find(str(i))] for line in crates_and_moves[:line_positions[1]] if line[line_positions[0].find(str(i))] != ' '] for i in range(1, 10)}

def move_crates(crates, number, origin, destination):
    crates[destination] = crates[origin][:number][::-1] + crates[destination]
    crates[origin] = crates[origin][number:]
    return crates

for move in moves:
    crates = move_crates(crates, **move)

''.join([crates[crate][0] for crate in crates])

def move_crates_9001(crates, number, origin, destination):
    crates[destination] = crates[origin][:number] + crates[destination]
    crates[origin] = crates[origin][number:]
    return crates

crates = {str(i): [line[line_positions[0].find(str(i))] for line in crates_and_moves[:line_positions[1]] if line[line_positions[0].find(str(i))] != ' '] for i in range(1, 10)}

for move in moves:
    crates = move_crates_9001(crates, **move)

''.join([crates[crate][0] for crate in crates])

