with open("input.txt") as f:
	texte = f.read().strip()

temp = [[j.split(" ") for j in i.splitlines()] for i in texte.split("\n\n")]
L = []
for claw in temp:
	a, b, p = claw
	L.append((int(a[2][2:-1]), int(a[3][2:]), int(b[2][2:-1]), int(b[3][2:]), int(p[1][2:-1]), int(p[2][2:])))

def solve(ax,ay,bx,by,px,py):
	det = ax*by - ay*bx
	i = (by*px-bx*py)/det
	j = (-ay*px+ax*py)/det
	if (i,j) == (int(i), int(j)):
		return 3*int(i)+int(j)
	return 0

res1 = sum(solve(ax,ay,bx,by,px,py) for (ax,ay,bx,by,px,py) in L)
res2 = sum(solve(ax,ay,bx,by,px+10000000000000,py+10000000000000) for (ax,ay,bx,by,px,py) in L)

print("Partie 1 :", res1)
print("Partie 2 :", res2)