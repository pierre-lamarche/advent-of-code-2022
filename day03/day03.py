import string

input = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day03/input.txt"

with open(input, mode='r') as f:
    backpacks = f.read().split("\n")

string.ascii_letters.find('a')

res = [string.ascii_letters.find(list(set(backpack[0:int(len(backpack)/2)]).intersection(set(backpack[int(len(backpack)/2):])))[0]) + 1
       for backpack in backpacks if backpack != '']
sum(res)

res = [string.ascii_letters.find(list(set(backpacks[i*3]).intersection(set(backpacks[i*3+1])).intersection(set(backpacks[i*3+2])))[0]) + 1
       for i in range(int(len(backpacks)/3))]
sum(res)