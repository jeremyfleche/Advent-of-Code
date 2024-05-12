from collections import deque

with open("input.txt") as f:
	texte = f.read()

# texte = """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ..........."""

grille = [[j for j in i] for i in texte.strip().splitlines()]

def start(grille):
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if grille[i][j] == 'S':
				return i,j

def solve(x,y,step):
	SEEN = {(x,y)}
	res = set()
	q = deque([(x,y,step)])
	while q:
		i,j,step = q.popleft()
		if step%2 == 0:
			res.add((i,j))
		if step == 0:
			continue
		for (a,b) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
			if 0<=a<len(grille) and 0<=b<len(grille[0]) and grille[a][b] != "#" and (a,b) not in SEEN and (a,b) not in res:
				SEEN.add((a,b))
				q.append((a,b,step-1))
	return len(res)

x,y = start(grille)
print('Partie 1 :',solve(x,y,64))

steps = 26501365
size = len(grille)

nb_grille = steps // size - 1

nb_grilles_impaires = (nb_grille // 2 * 2 + 1) ** 2
nb_grilles_paires = ((nb_grille+1) // 2 * 2) ** 2

points_impaires = solve(x,y,size*2 + 1)
points_pairs = solve(x,y, size*2)

coin_h = solve(x, size-1, size-1)
coin_b = solve(x, 0, size-1)
coin_d = solve(size-1, y, size-1)
coin_g = solve(0, y, size-1)

petit_morceau_hd = solve(0, size-1, size // 2 - 1)
petit_morceau_bd = solve(0, 0, size // 2 - 1)
petit_morceau_hg = solve(size-1, size-1, size // 2 - 1)
petit_morceau_bg = solve(size-1, 0, size // 2 - 1)

petit_morceau_hd = solve(0, size-1, size // 2 - 1)
petit_morceau_bd = solve(0, 0, size // 2 - 1)
petit_morceau_hg = solve(size-1, size-1, size // 2 - 1)
petit_morceau_bg = solve(size-1, 0, size // 2 - 1)

grand_morceau_hd = solve(0, size-1, size*3 // 2 - 1)
grand_morceau_bd = solve(0, 0, size*3 // 2 - 1)
grand_morceau_hg = solve(size-1, size-1, size*3 // 2 - 1)
grand_morceau_bg = solve(size-1, 0, size*3 // 2 - 1)


res = (
	nb_grilles_impaires * points_impaires +
	nb_grilles_paires * points_pairs +
	coin_h + coin_b + coin_d + coin_g +
	(nb_grille + 1) * (petit_morceau_hd + petit_morceau_bd + petit_morceau_hg + petit_morceau_bg) +
	nb_grille * (grand_morceau_hd + grand_morceau_bd + grand_morceau_hg + grand_morceau_bg)
	)

print("Partie 2 :",res)