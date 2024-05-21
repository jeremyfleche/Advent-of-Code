with open("input.txt") as f:
	texte = f.read()

texte = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

temp = texte.strip().split("\n\n")

molecule = temp[0]
transformation = {a:b for a,b in [[j for j in i.split(" -> ")] for i in temp[1].splitlines()]}

d = {i:0 for i in transformation.values()}
for i in molecule:
	d[i] += 1

def algo(molecule, step, stop):
	if step <= stop:
		a = transformation[molecule]
		d[a] += 1
		algo(molecule[0]+a,step+1, stop)
		algo(a+molecule[1],step+1, stop)

for i in range(len(molecule)-1):
	algo(molecule[i]+molecule[i+1],1,10)

print("Partie 1 :",max(d.values())-min(d.values()))

count = dict()
for i in molecule:
	count[i] = (1 if i not in count else count[i]+1)

step_count = dict()
for i in range(len(molecule)-1):
	step_count[molecule[i]+molecule[i+1]] = 1

for _ in range(40):
	temp_step_count = dict()
	for m,v in step_count.items():
		temp_step_count[m[0]+transformation[m]] = (v if m[0]+transformation[m] not in temp_step_count else temp_step_count[m[0]+transformation[m]]+v)
		temp_step_count[transformation[m]+m[1]] = (v if transformation[m]+m[1] not in temp_step_count else temp_step_count[transformation[m]+m[1]]+v)
		count[transformation[m]] = (v if transformation[m] not in count else count[transformation[m]]+v)
	step_count = temp_step_count

print("Partie 2 :",max(count.values())-min(count.values()))