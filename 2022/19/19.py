with open('input.txt','r') as f:
	texte = f.read()

"""
texte = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''
"""

t = [i.split(' ') for i in texte.split('\n') if i!=""]

for i in range(len(t)):
	t[i] = [int(t[i][1][:-1]),int(t[i][6]),int(t[i][12]),int(t[i][18]),int(t[i][21]),int(t[i][27]),int(t[i][30])]

def solve(Co,Cc,Co1,Co2,Cg1,Cg2,t):
	best = 0
	init = (0,0,0,0,1,0,0,0,t)
	Q = [init]
	seen = set()
	Core = max([Co, Cc, Co1, Cg1])
	while Q:
		temp = Q.pop()
		ore,clay,obsidian,geode,r1,r2,r3,r4,t = temp
		
		best = max(best, geode)
		if t==0:
			continue
		
		if r1>=Core:
			r1 = Core
		if r2>=Co2:
			r2 = Co2
		if r3>=Cg2:
			r3 = Cg2
		if ore >= t*Core-r1*(t-1):
			ore = t*Core-r1*(t-1)
		if clay>=t*Co2-r2*(t-1):
			clay = t*Co2 - r2*(t-1)
		if obsidian>=t*Cg2-r3*(t-1):
			obsidian = t*Cg2-r3*(t-1)

		temp = (ore,clay,obsidian,geode,r1,r2,r3,r4,t)

		if temp in seen:
			continue
		seen.add(temp)


		Q.append((ore+r1,clay+r2,obsidian+r3,geode+r4,r1,r2,r3,r4,t-1))
		if ore >= Co:
			Q.append((ore-Co+r1,clay+r2,obsidian+r3,geode+r4,r1+1,r2,r3,r4,t-1))
		if ore >= Cc:
			Q.append((ore-Cc+r1,clay+r2,obsidian+r3,geode+r4,r1,r2+1,r3,r4,t-1))
		if ore >= Co1 and clay >= Co2:
			Q.append((ore-Co1+r1,clay-Co2+r2,obsidian+r3,geode+r4,r1,r2,r3+1,r4,t-1))
		if ore >= Cg1 and obsidian >= Cg2:
			Q.append((ore-Cg1+r1,clay+r2,obsidian-Cg2+r3,geode+r4,r1,r2,r3,r4+1,t-1))
	return best

res1 = 0
res2 = 1
for ligne in t:
	i,Co,Cc,Co1,Co2,Cg1,Cg2 = ligne
	res1 += solve(Co,Cc,Co1,Co2,Cg1,Cg2,24)*i
	if i<=3:
		res2 *= solve(Co,Cc,Co1,Co2,Cg1,Cg2,32)

print('Partie 1 :',res1)	# attendre environ 35 secondes
print('Partie 2 :',res2)