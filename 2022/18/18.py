from math import inf

with open('input.txt','r') as f:
	texte = f.read()

t = [[int(j) for j in i.split(',')] for i in texte.split('\n') if i!='']

res = 0
E = set([(x,y,z) for (x,y,z) in t])
for (x,y,z) in t:
	if (x+1,y,z) not in E:
		res+=1
	if (x-1,y,z) not in E:
		res+=1
	if (x,y+1,z) not in E:
		res+=1
	if (x,y-1,z) not in E:
		res+=1
	if (x,y,z+1) not in E:
		res+=1
	if (x,y,z-1) not in E:
		res+=1

print('Partie 1 :',res)

# Partie 2

def bord(x,y,z):
	if (x,y,z) in IN:
		return False
	if (x,y,z) in OUT:
		return True
	deja_vu = set()
	Q = [(x,y,z)]
	while Q:
		x,y,z = Q[0]
		del Q[0]
		if (x,y,z) in E or (x,y,z) in deja_vu:
			continue
		deja_vu.add((x,y,z))
		if len(deja_vu) >= len(t):
			for i in deja_vu:
				OUT.add(i)
			return True
		Q.append((x+1,y,z))
		Q.append((x-1,y,z))
		Q.append((x,y+1,z))
		Q.append((x,y-1,z))
		Q.append((x,y,z+1))
		Q.append((x,y,z-1))

	for i in deja_vu:
		IN.add(i)
	return False

res = 0
OUT = set()
IN = set()
E = set([(x,y,z) for (x,y,z) in t])
for (x,y,z) in t:
	if bord(x+1,y,z):
		res+=1
	if bord(x-1,y,z):
		res+=1
	if bord(x,y+1,z):
		res+=1
	if bord(x,y-1,z):
		res+=1
	if bord(x,y,z+1):
		res+=1
	if bord(x,y,z-1):
		res+=1

print('Partie 2 :',res)
