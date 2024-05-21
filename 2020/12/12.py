with open("input.txt") as f:
	texte = f.read()

# texte = """F10
# N3
# F7
# R90
# F11"""

instructions = [(i[0],int(i[1:])) for i in texte.strip().split("\n")]

def change_facing(valeur):
	global i_facing
	global facing
	global current_facing
	i_facing = (i_facing+(valeur//90))%4
	current_facing = facing[i_facing]

def avancer(position, valeur):
	global current_facing
	x, y = position
	if current_facing == "North":
		return x, y-valeur
	if current_facing == "South":
		return x, y+valeur
	if current_facing == "West":
		return x-valeur, y
	if current_facing == "East":
		return x+valeur, y

def commandes(instruction,position):
	lettre, valeur = instruction
	x, y = position
	if lettre == "N":
		return x, y-valeur
	if lettre == "S":
		return x, y+valeur
	if lettre == "W":
		return x-valeur, y
	if lettre == "E":
		return x+valeur, y
	if lettre == "R":
		change_facing(valeur)
		return x, y
	if lettre == "L":
		change_facing(-valeur)
		return x, y
	if lettre == "F":
		return avancer(position, valeur)

facing = ["North", "East", "South", "West"]
i_facing = 1
current_facing = facing[i_facing]
position = (0,0)

for i in instructions:
	position = commandes(i,position)

print("Partie 1 :",abs(position[0])+abs(position[1]))

#Partie 2

waypoint = (10,-1)
position = (0,0)

def turn(waypoint, valeur):
	i = valeur // 90
	if i < 0:
		i = 4 + i 			# i est déjà négatif
	for _ in range(i):
		xw, yw = waypoint
		waypoint = -yw, xw
	return waypoint

def avancer2(waypoint,position,valeur):
	x, y = position
	xw, yw = waypoint
	return x+xw*valeur, y+yw*valeur

def commandes2(instruction):
	global position
	global waypoint
	lettre, valeur = instruction
	x, y = position
	xw, yw = waypoint
	if lettre == "N":
		waypoint = xw, yw-valeur
	if lettre == "S":
		waypoint = xw, yw+valeur
	if lettre == "W":
		waypoint = xw-valeur, yw
	if lettre == "E":
		waypoint = xw+valeur, yw
	if lettre == "R":
		waypoint = turn(waypoint,valeur)
	if lettre == "L":
		waypoint = turn(waypoint,-valeur)
	if lettre == "F":
		position = avancer2(waypoint,position,valeur)

for i in instructions:
	commandes2(i)

print("Partie 2 :",abs(position[0])+abs(position[1]))