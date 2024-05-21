from math import inf

with open('input.txt','r') as f:
	texte = f.read()

t = [i.split(' ') for i in texte.split('\n') if i!='']

for ligne in range(len(t)):
	t[ligne] = [int(t[ligne][2][2:-1]),int(t[ligne][3][2:-1]),int(t[ligne][8][2:len(t[ligne][8])-1]),int(t[ligne][9][2:])]

def distance(a,b):
	xa, ya = a
	xb ,yb = b
	return abs(yb-ya) + abs(xb-xa)

def dimension(d):
	mini_x = inf
	maxi_x = 0
	for i in d:
		x,y = i
		if x - distance(i,d[i]) < mini_x:
			mini_x = x - distance(i,d[i])
		if x + distance(i,d[i]) > maxi_x:
			maxi_x = x + distance(i,d[i])
	return mini_x,maxi_x

d = dict()
E = set()
for ligne in t:
	d[(ligne[0],ligne[1])] = (ligne[2],ligne[3])
	E.add((ligne[0],ligne[1],distance((ligne[0],ligne[1]),(ligne[2],ligne[3]))))

print("Le temps total pour les deux parties est d'environ 2 min 30")

res = 0
y = 2000000
mini_x, maxi_x = dimension(d)
for x in range(mini_x, maxi_x+1):
	if x % 100000 == 0:
		print('Partie 1 :',round((x+abs(mini_x))*100/(abs(mini_x)+abs(maxi_x)),1),'%')
	for i in d:
		if (x,y) == d[i] or (x,y) == i:
			break
		elif distance(i,(x,y)) <= distance(i,d[i]):
			res += 1
			break

print('Partie 1 :',res)
print('Maintenant, attendre environ 90 secondes de plus pour la partie 2')

def valide(x,y,E):
	for ex,ey,d in E:
		if distance((x,y),(ex,ey)) <= d:
			return False
	return True

def part2(E):
	R = set()
	for ex,ey,d in E:
		for dx in range(d+2):
			dy = d-dx+1
			for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
				x = ex + signx*dx
				y = ey + signy*dy
				if valide(x,y,E) and 0<=x<=4000000 and 0<=y<=4000000:
					return x*4000000+y
		R.add((ex,ey,d))

print('Partie 2 :',part2(E))