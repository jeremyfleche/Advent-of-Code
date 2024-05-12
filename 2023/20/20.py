from collections import deque
from math import gcd

with open("input.txt") as f:
	texte = f.read()

# texte = """broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output"""

# Suivant(s) de chaque module
connexions = {i.split('->')[0].strip(): [j.strip() for j in i.split('->')[1].split(',')] for i in texte.strip().splitlines()}

# Valeur actuelle de chaque module
outputs = {i.strip("%&"):0 for i in connexions}

# Mémoire de chaque conjonction -> valeur la plus récente de tous leurs inputs
conjonctions = {i.strip("%&"):{j.strip("%&"):0 for j in connexions if i[1:] in connexions[j]} for i in connexions if i[0]=='&'}

# compteur de singaux high (1) et lows (0)
count = {0:0, 1:0}

def conjonction_valide(c):
	return all(conjonctions[c][i] == 1 for i in conjonctions[c])

output_part2 = 'rx'

for i in connexions:
	if output_part2 in connexions[i]:
		precedent_rx = i[1:]
		break

# Pour la partie 2
longueur_cycle = {}
seen = {i[1:]:0 for i in connexions if precedent_rx in connexions[i]}

push = 1
while True:
	Q = deque([('button','broadcaster',0)])
	while Q:
		sender, module, signal = Q.popleft()
		count[signal] += 1
		
		if module == precedent_rx and signal == 1:
			seen[sender] += 1

			if sender not in longueur_cycle:
				longueur_cycle[sender] = push

			if all(seen.values()):
				x = 1
				for i in longueur_cycle.values():
					x = x*i // gcd(x,i)
				print("Partie 2 :",x)
				exit(0)

		if module == "broadcaster":
			for i in connexions[module]:
				Q.append((module, i, signal))
		elif '%'+module in connexions:
			if signal == 0:
				outputs[module] = 1 - outputs[module]
				for i in connexions['%'+module]:
					Q.append((module, i, outputs[module]))
		elif '&'+module in connexions:
			conjonctions[module][sender] = signal
			new_signal = 0 if all(conjonctions[module][i]==1 for i in conjonctions[module]) else 1
			for i in connexions['&'+module]:
				Q.append((module, i, new_signal))
	if push == 1000:
		print("Partie 1 :",count[0]*count[1])
	push += 1

# Partie 2