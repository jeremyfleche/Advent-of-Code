target_area = (211,232,-124,-69)
# target_area = (20,30,-10,-5)

def in_target_area(x,y):
	x1, x2, y1, y2 = target_area
	if x1<=x<=x2 and y1<=y<=y2:
		return True
	return False

def ratee(x,y):
	x1, x2, y1, y2 = target_area
	if x2<x or y1>y:
		return True
	return False

def somme_decroissante(x):
	if x == 1:
		return 1
	return x + somme_decroissante(x-1)

# Calcule la plus grande valeur de vx possible
vx_min = 1
vx_max = target_area[1]
while somme_decroissante(vx_min) < target_area[0]:
	vx_min += 1

vy_min = target_area[2]
vy_max = 1000

def tir(vx,vy):
	x = 0
	y = 0
	maximum = 0
	while True:
		x += vx
		y += vy
		vx = (vx-1 if vx > 0 else 0)
		vy -= 1
		if y > maximum:
			maximum = y
		if in_target_area(x,y):
			return maximum
		if ratee(x,y):
			return -1

hauteur_max = 0
res2 = 0
for vx in range(vx_min, vx_max+1):
	for vy in range(vy_min, vy_max+1):
		if tir(vx,vy) > hauteur_max:
			hauteur_max = tir(vx,vy)
		if tir(vx,vy) > -1:
			res2 += 1

print("Partie 1 :",hauteur_max)
print("Partie 2 :", res2)