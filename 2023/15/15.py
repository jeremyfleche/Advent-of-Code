with open("input.txt") as f:
	texte = f.read()

# texte = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

t = texte.strip().split(",")

def HASH(mot):
	res = 0
	for c in mot:
		res = (res+ord(c))*17%256
	return res

res = 0
for mot in t:
	res += HASH(mot)

print("Partie 1 :",res)

def mot_in(mot,d,box):
	for i in range(len(d[box])):
		(m,_) = d[box][i]
		if mot == m:
			return i
	return -1

d = {i:[] for i in range(256)}
for mot in t:
	if '=' in mot:
		m,b = mot.split("=")
		box = HASH(m)
		value = int(b)
		x = mot_in(m,d,box)
		if x == -1:
			d[box].append((m,value))
		else:
			d[box][x] = (m,value)
	else:
		m = mot[:-1]
		box = HASH(m)
		for (mot,x) in d[box]:
			if mot == m:
				d[box].remove((mot,x))

res = 0
for box in d:
	for i in range(len(d[box])):
		_,x = d[box][i]
		res += (box+1)*(i+1)*x

print("Partie 2 :",res)