with open("input.txt") as f:
	texte = f.read().strip()

x_size, y_size = 101, 103

# x_size, y_size = 11, 7
# texte = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""

robots = []
for line in texte.splitlines():
	temp = line.split(" ")
	a, b = temp[0].split(",")
	c, d = temp[1].split(",")
	robots.append([int(a[2:]), int(b), int(c[2:]), int(d)])

def affichage(robots):
	G = [[" " for _ in range(x_size)] for _ in range(y_size)]
	for x,y,_,_ in robots:
		G[y][x] = "#"
	for line in G:
		for c in line:
			print(c, end="")
		print()

def part1():
	a,b,c,d = 0,0,0,0
	for x,y,_,_ in robots:
		if x < x_size//2 and y < y_size//2:
			a += 1
		elif x > x_size//2 and y < y_size//2:
			b += 1
		elif x < x_size//2 and y > y_size//2:
			c += 1
		elif x > x_size//2 and y > y_size//2:
			d += 1
	return a*b*c*d

def easter_egg(robots):
	E = set((x,y) for x,y,_,_ in robots)
	k = 0
	for x,y,_,_ in robots:
		complete_node = True
		for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (x+i,y+j) not in E:
				complete_node = False
				break
		if complete_node:
			k += 1
	if k > 20:	# S'il y a plus de 20 robots (nombre choisi arbitrairement) qui ont un voisins dans les 4 directions, on peut supposer qu'on est sur l'easter egg
		return True
	return False

seconds = 0
while not easter_egg(robots):
	for i in range(len(robots)):
		x,y,vx,vy = robots[i]
		robots[i] = [(x+vx)%x_size,(y+vy)%y_size, vx,vy]
	seconds += 1
	if seconds == 100:
		res1 = part1()

affichage(robots)
print("Partie 1 :", res1)
print("Partie 2 :", seconds)