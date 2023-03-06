import sys
sys.setrecursionlimit(999999999)


def print_liste(liste):
    print("--" * len(liste) + "---")
    for ligne in liste:
        print("|", *ligne, "|", sep='')
    print("--" * len(liste) + "---")

def expansion(liste, points):
    if points == []:
        return liste
    taille, taches = len(liste)-1, []
    for x, y, logo in points:
        for x1, y1 in [(1+x, 0+y), (0+x, 1+y), (-1+x, 0+y), (0+x, -1+y)]:
            if 0 <= x1 <= taille and 0 <= y1 <= taille and liste[y1][x1] == "-":
                liste[y1][x1] = logo
                taches.append((x1, y1, logo))
    return expansion(liste, taches)


l = 100
electorat = [ ["-" for _ in range(l)] for _ in range(l)]
points = [(3, 5, "X"), (4, 2, "P"), (9, 5, "C"), (2, 9, "E")]

for point in points:
    electorat[point[1]][point[0]] = point[2]

print_liste(expansion(electorat, points))