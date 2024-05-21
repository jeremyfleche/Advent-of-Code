from collections import deque

with open("input.txt") as f:
	texte = f.read()

# texte = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

arcs = [[j for j in i.split("-")] for i in texte.strip().splitlines()]

def grottes():
	E = set()
	for arc in arcs:
		for grotte in arc:
			E.add(grotte)
	return E

grottes = grottes()

def voisins(grotte):
	E = set()
	for arc in arcs:
		if grotte in arc:
			E.add((arc[0]) if arc[1] == grotte else arc[1])
	return E

def isvalid(chemin):
	if chemin[0] != "start":
		return False
	d = dict()
	for i in chemin:
		try:
			d[i] += 1
			if i.islower():
				return False
		except:
			d[i] = 1
	return True

def isdone(chemin):
	if chemin[-1] == "end":
		return True
	return False

def cheminToStr(chemin):
	s = ""
	for i in chemin:
		s += i
		s += " "
	return s

def algo():
	chemins = deque([["start"]])
	fini = dict()
	while chemins:
		chemin_courant = chemins.popleft()
		try:
			if fini[cheminToStr(chemin_courant)] == 1:
				pass
		except:
			grotte = chemin_courant[-1]
			for i in voisins(grotte):
				if isvalid(chemin_courant + [i]) and isdone(chemin_courant + [i]):
					fini[cheminToStr(chemin_courant+[i])] = 1
				if isvalid(chemin_courant + [i]):
					chemins.append(chemin_courant + [i])

	return len(fini)

print("Partie 1 :",algo())

def isvalid2(chemin):
	if chemin[0] != "start":
		return False
	d = dict()
	joker = True
	for i in chemin:
		try:
			d[i] += 1
			if i in ["start","end"]:
				return False
			elif i.islower() and not joker:
				return False
			elif i.islower() and joker:
				d[i] += 1
				joker = False
		except:
			d[i] = 1
	return True

def algo2():
	chemins = deque([["start"]])
	fini = dict()
	while chemins:
		chemin_courant = chemins.popleft()
		try:
			if fini[cheminToStr(chemin_courant)] == 1:
				pass
		except:
			grotte = chemin_courant[-1]
			for i in voisins(grotte):
				if isvalid2(chemin_courant + [i]) and isdone(chemin_courant + [i]):
					fini[cheminToStr(chemin_courant+[i])] = 1
				if isvalid2(chemin_courant + [i]):
					chemins.append(chemin_courant + [i])

	return len(fini)

# Attendre environ 17 sec pour la partie 2
print("Partie 2 :",algo2())