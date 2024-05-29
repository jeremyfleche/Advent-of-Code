def play(position, score, player, die, roll):
	mouv = 0
	for _ in range(3):
		mouv += die
		die = die+1 if die != 100 else 1
	position[player] += mouv%10
	if position[player] > 10:
		position[player] -= 10
	score[player] += position[player]
	return position, score, die, roll+3

with open("input.txt") as f:
	texte = f.read().strip()

position = [int(ligne.split()[-1]) for ligne in texte.splitlines()]
score = [0, 0]
die = 1
roll = 0
i = 0

while True:
	position, score, die, roll = play(position, score, i, die, roll)
	if score[i] >= 1000:
		print("Partie 1 :", score[1-i]*roll)
		break
	i = 1-i

# Partie 2

position = [int(ligne.split()[-1]) for ligne in texte.splitlines()]
score = [0, 0]
cache = dict()

def solve(position, score, player):
	global cache
	data = tuple(position + score + [player])
	if score[1-player] >= 21:
		return (1, 0, player) if player == 1 else (0, 1, player)
	
	if data in cache:
		return cache[data]
	
	temp = [0, 0, player]
	for a in range(1, 4):
		for b in range(1, 4):
			for c in range(1, 4):
				new_pos = [position[0], position[1]]
				new_score = [score[0], score[1]]
				
				new_pos[player] = new_pos[player]+a+b+c if new_pos[player]+a+b+c <= 10 else new_pos[player]+a+b+c-10 
				new_score[player] += new_pos[player]

				x,y, _ = solve(new_pos, new_score, 1-player)
				temp[0] += x
				temp[1] += y
	
	cache[data] = temp	
	return cache[data]

print("Partie 2 :",max(solve(position, score, 0)))