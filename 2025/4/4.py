import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

grille = [[i for i in line] for line in texte.splitlines()]

def solve(part2=False):
    res = 0
    change = True
    while (change):
        change = False
        for i in range(len(grille)):
            for j in range(len(grille[0])):
                if grille[i][j] == '@':
                    voisins = 0
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            try:
                                if (i+di)>=0 and (j+dj)>=0 and grille[i+di][j+dj] == '@':
                                    voisins += 1
                            except:
                                pass
                    if voisins-1<4:
                        if part2:
                            grille[i][j] = '.'
                            change = True
                        res += 1
    return res


print("Partie 1 :",solve())
print("Partie 2 :",solve(part2=True))
print(f"[{int((time.time()-START_TIME)*1000)}ms]")
