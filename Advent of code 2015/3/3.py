with open('input.txt','r') as f:
	texte = f.read()

t = texte.strip()
E = {(0,0)}
x,y = 0,0
for i in t:
	if i == '<':
		x -= 1
	if i == '>':
		x += 1
	if i == 'v':
		y += 1
	if i == '^':
		y -= 1
	E.add((x,y))

print('Partie 1 :',len(E))

E = {(0,0)}
xs,ys = 0,0
xr,yr = 0,0
for i in range(len(t)):
	if i%2==1:
		if t[i] == '<':
			xs -= 1
		if t[i] == '>':
			xs += 1
		if t[i] == 'v':
			ys += 1
		if t[i] == '^':
			ys -= 1
		E.add((xs,ys))
	else:
		if t[i] == '<':
			xr -= 1
		if t[i] == '>':
			xr += 1
		if t[i] == 'v':
			yr += 1
		if t[i] == '^':
			yr -= 1
		E.add((xr,yr))

print('Partie 2 :',len(E))