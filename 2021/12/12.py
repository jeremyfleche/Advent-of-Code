with open("input.txt") as f:
	texte = f.read()

texte = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

chemins = [i.split("-") for i in texte.strip().splitlines()]

def grottes_suivantes(grotte):
	res = []
	for lien in chemins:
		try:
			res.append(lien[1 - lien.index(grotte)])
		except:
			pass
	return res

def grotte_minuscule(grotte):
	if grotte.islower() and grotte not in ('start', 'end'):
		return True
	return False

