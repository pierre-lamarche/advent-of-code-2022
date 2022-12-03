fichier = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day02/input.txt"

with open(fichier, mode='r') as f:
    jeux = [jeu.split(' ') for jeu in f.read().split("\n") if jeu != '']

valeurs_opposant = ['A', 'B', 'C']
valeurs_joueur = ['X', 'Y', 'Z']
scores = [3, 6, 0]

def resultat(opposant, joueur):
    opp = valeurs_opposant.index(opposant)
    jou = valeurs_joueur.index(joueur)
    return scores[jou - opp] + jou + 1

sum([resultat(jeu[0], jeu[1]) for jeu in jeux])

def resultat2(opposant, outcome):
    score = scores[valeurs_joueur.index(outcome) - 1]
    return score + valeurs_joueur.index(valeurs_joueur[(valeurs_opposant.index(opposant) + valeurs_joueur.index(outcome) - 1) % 3]) + 1

sum([resultat2(jeu[0], jeu[1]) for jeu in jeux])

