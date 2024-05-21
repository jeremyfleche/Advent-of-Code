with open('input.txt','r') as f:
	texte = f.read().strip()

#texte = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''
t = [(-1 if x=='<' else 1) for x in texte]

def piece(nb_rocher,d):
	a = min([y for (x,y) in d]) - 4
	if nb_rocher % 5 == 0:
		return {(2,a),(3,a),(4,a),(5,a)}
	elif nb_rocher % 5 == 1:
		return {(2,a-1),(3,a),(3,a-1),(3,a-2),(4,a-1)}
	elif nb_rocher % 5 == 2:
		return {(2,a),(3,a),(4,a),(4,a-1),(4,a-2)}
	elif nb_rocher % 5 == 3:
		return {(2,a),(2,a-1),(2,a-2),(2,a-3)}
	else:
		return {(2,a),(2,a-1),(3,a),(3,a-1)}

def top_shape(d):
	res = [0] * 7
	for (x,y) in d:
		res[x] = max(res[x],y)
	top = max(res)
	bottom = min(res)
	return tuple(top-x for (x,y) in d if bottom<=y<=top)

def solve(part):
	d = set()
	for x in range(7):
		d.add((x,0))
	seen = dict()
	taille = 0
	nb_rocher = 0
	i = 0
	X = (2022 if part == 1 else 1000000000000)
	rocher = piece(nb_rocher,d)
	while nb_rocher < X:
		moved = {(x+t[i],y) for (x,y) in rocher}
		if all(0 <= x <= 6 for (x,y) in moved) and not (d & moved): # si le nouveau rocher n'est pas sorti de la grille et n'est pas entré en collisison avec la structure existante
			rocher = moved
		i = (i+1)%len(t)
		moved = {(x,y+1) for (x,y) in rocher}
		if d & moved:
			d |= rocher
			taille = abs(min([y for (x,y) in d]))
			nb_rocher += 1
			temp = (i, nb_rocher%5, top_shape(d))
			if temp in seen and part == 2:
				last_nb_rocher,last_taille = seen[temp]
				rep = (X - nb_rocher) // (nb_rocher - last_nb_rocher)
				offset = rep * (taille - last_taille)
				nb_rocher += rep * (nb_rocher - last_nb_rocher)
				seen = dict()
			seen[temp] = (nb_rocher,taille)
			rocher = piece(nb_rocher,d)
		else:
			rocher = moved
	return (taille if part == 1 else taille + offset)

print('Partie 1 :',solve(1))
print('Partie 2 :',solve(2))