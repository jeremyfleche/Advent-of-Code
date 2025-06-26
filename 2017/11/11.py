with open("input.txt") as f:
	texte = f.read().strip()

instructions = texte.split(',')

def point_arrivée():
	x,y = 0,0
	d = {'n':(0,1), 'ne':(1, 0.5), 'se':(1, -0.5), 's':(0,-1), 'sw':(-1,-0.5), 'nw':(-1,0.5)}
	for i in instructions:
		dx, dy = d[i]
		x += dx
		y += dy
	return x,y

def distance(p):
	x,y = p
	if abs(x) >= 2*abs(y):
		return abs(x)
	return 1 + distance((x, abs(y)-1))

def part1():
	return distance(point_arrivée())

def part2():
	x,y = 0,0
	res = 0
	d = {'n':(0,1), 'ne':(1, 0.5), 'se':(1, -0.5), 's':(0,-1), 'sw':(-1,-0.5), 'nw':(-1,0.5)}
	for i in instructions:
		dx, dy = d[i]
		x += dx
		y += dy
		res = max(res, distance((x,y)))
	return res

print("Partie 1 :", part1())
print("Partie 2 :", part2())