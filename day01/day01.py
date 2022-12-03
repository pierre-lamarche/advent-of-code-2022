fichier = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day01/input.txt"

with open(fichier, mode='r') as f:
    puzzle = f.read().split('\n')

somme = []
somme_partielle = 0
for case in puzzle:
    if case != '':
        somme_partielle += int(case)
    else:
        somme.append(somme_partielle)
        somme_partielle = 0
somme.append(somme_partielle)
max(somme)

somme.sort()
sum(somme[-3:])

## plus rapide

with open(fichier, mode='r') as f:
    puzzle = f.read().split('\n\n')

somme = [sum([int(c) for c in case.split('\n') if c != '']) for case in puzzle]
max(somme)

somme.sort()
sum(somme[-3:])