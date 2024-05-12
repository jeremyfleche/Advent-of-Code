import sympy

with open("input.txt") as f:
	texte = f.read()

# texte = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3"""

t = [[int(j.strip(',')) for j in i.split() if j!='@'] for i in texte.strip().splitlines()]

def collisions(ligne1, ligne2):
	x1, y1, _, vx1, vy1, _ = ligne1
	x2, y2, _, vx2, vy2, _ = ligne2
	a1 = vy1
	b1 = -vx1
	c1 = vy1*x1 - vx1*y1
	a2 = vy2
	b2 = -vx2
	c2 = vy2*x2 - vx2*y2
	denominateur = a1*b2 - a2*b1
	if denominateur == 0:
		return None,None
	x = (c1*b2 - c2*b1) / denominateur
	y = (a1*c2 - a2*c1) / denominateur
	if (x - x1)*vx1 >= 0 and (y - y1)*vy1 >= 0:
		if (x - x2)*vx2 >= 0 and (y - y2)*vy2 >= 0:
			return x,y
	return None,None

res = 0
for i in range(len(t)):
	for j in range(i+1,len(t)):
		x,y = collisions(t[i],t[j])
		if x != None:
			if 200000000000000<=x<=400000000000000 and 200000000000000<=y<=400000000000000:
				res += 1

print("Partie 1:",res)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i,(sx,sy,sz,vx,vy,vz) in enumerate(t):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
    	continue
    res = sympy.solve(equations)
    if len(res) == 1:
    	res = res[0]
    	print("Partie 2:",res[xr]+res[yr]+res[zr])
    	break