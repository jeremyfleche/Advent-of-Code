nombre=368078
x,y=0,0
pas=1
cible=1
while cible!=nombre:
	for i in range(abs(pas)):
		x+=1
		cible+=1
		if cible==nombre:
			break
	if cible==nombre:
		break
	for i in range(abs(pas)):
		y+=1
		cible+=1
		if cible==nombre:
			break
	if cible==nombre:
		break

	pas+=1

	for i in range(abs(pas)):
		x-=1
		cible+=1
		if cible==nombre:
			break
	if cible==nombre:
		break
	for i in range(abs(pas)):
		y-=1
		cible+=1
		if cible==nombre:
			break
	if cible==nombre:
		break

	pas+=1
	

print('Partie 1 :',abs(x)+abs(y))

#partie 2

nombre=368078

def grille(nombre):
	pas=1
	x=0
	while x<nombre:
		x+=2*pas
		pas+=1

	res=[]
	for i in range(pas+1):
		res.append([])
		for j in range(pas+1):
			res[len(res)-1].append(0)

	return res

def somme(grille,i,j):
	res=0
	for x in range(-1,2):
		for y in range(-1,2):
			res+=grille[i+x][j+y]
	return res

grille = grille(nombre)
x = y = len(grille)//2
pas = 1
grille[x][y] = 1

while True:

	for i in range(pas):
		x+=1
		grille[x][y]=somme(grille,x,y)
		if grille[x][y]>nombre:
			print('Partie 2 :',grille[x][y])
			break

	if grille[x][y]>nombre:
		break

	for i in range(pas):
		y+=1
		grille[x][y]=somme(grille,x,y)
		if grille[x][y]>nombre:
			print('Partie 2 :',grille[x][y])
			break

	if grille[x][y]>nombre:
		break

	pas+=1

	for i in range(pas):
		x-=1
		grille[x][y]=somme(grille,x,y)
		if grille[x][y]>nombre:
			print('Partie 2 :',grille[x][y])
			break

	if grille[x][y]>nombre:
		break

	for i in range(pas):
		y-=1
		grille[x][y]=somme(grille,x,y)
		if grille[x][y]>nombre:
			print('Partie 2 :',grille[x][y])
			break

	if grille[x][y]>nombre:
		break

	pas+=1