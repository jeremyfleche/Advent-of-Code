from collections import deque

with open("input.txt") as f:
	texte = f.read()

# texte = """1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9"""

grille = [[tuple(int(k) for k in j.split(',')) for j in i .split('~')] for i in texte.splitlines()]

di = dict()
E = dict()
for i in range(len(grille)):
	a,b,c = grille[i][0]
	d,e,f = grille[i][1]
	block = []
	for x in range(a,d+1):
		for y in range(b,e+1):
			for z in range(c,f+1):
				E[(x,y,z)] = i
				block.append((x,y,z))
	di[i] = block

def peut_tomber(i, di, E):
	for (x,y,z) in di[i]:
		if z == 1 or ((x,y,z-1) in E and E[(x,y,z-1)] != i):
			return False
	return True

def doient_tomber(di,E):
	liste = []
	for i in di:
		if peut_tomber(i,di, E):
			liste.append(i)
	return liste

x = doient_tomber(di,E)
while x != []:
	for i in x:
		temp = dict()
		for j in range(len(di[i])):
			x,y,z = di[i][j]
			di[i][j] = (x,y,z-1)
			temp[(x,y,z-1)] = i
			del E[(x,y,z)]
		E |= temp
	x = doient_tomber(di,E)

def est_inutile(i, dessus, dessous):
	if len(dessus[i]) == 0:
		return True
	for j in dessus[i]:
		if dessous[j] == {i}:
			return False
	return True

def reactionEnChaine(i,dessus,dessous):
	Q = deque(list(dessus[i]))
	res = {i}
	while Q:
		i = Q.popleft()
		if i in res:
			continue
		if all(x in res for x in dessous[i]):
			res.add(i)
			for j in dessus[i]:
				Q.append(j)
	return len(res)-1							# On enlève block qu'on est en train de tester car on le met dans res ligne 64

dessus = dict()
dessous = dict()
for i in di:
	temp_dessus = set()
	temp_dessous = set()
	for (x,y,z) in di[i]:
		if z > 1 and (x,y,z-1) in E and E[(x,y,z-1)] != i:
			temp_dessous.add(E[(x,y,z-1)])
		if (x,y,z+1) in E and E[(x,y,z+1)] != i:
			temp_dessus.add(E[(x,y,z+1)])
	dessus[i] = temp_dessus
	dessous[i] = temp_dessous

res1 = 0
res2 = 0
for i in di:
	if est_inutile(i, dessus, dessous):
		res1 += 1
	else:
		res2 += reactionEnChaine(i,dessus,dessous)

print("Partie 1 :",res1)
print("Partie 2 :",res2)
