with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''
"""
t = [i.split(' ') for i in texte.split('\n') if i != '']

for ligne in range(len(t)):
	t[ligne] = [t[ligne][0][:-1]]+t[ligne][1:]

d = dict()
for ligne in t:
	if len(ligne) == 2:
		d[ligne[0]] = int(ligne[1])
	else:
		d[ligne[0]] = []
		for i in range(1,len(ligne)):
			d[ligne[0]].append(ligne[i])

def solve(root,h):
	if root == 'humn' and h >= 0:
		return h
	elif type(d[root]) == int:
		return d[root]
	else:
		if d[root][1] == '*':
			return solve(d[root][0],h)*solve(d[root][2],h)
		if d[root][1] == '/':
			return solve(d[root][0],h)/solve(d[root][2],h)
		if d[root][1] == '+':
			return solve(d[root][0],h)+solve(d[root][2],h)
		if d[root][1] == '-':
			return solve(d[root][0],h)-solve(d[root][2],h)

print('Partie 1 :',int(solve('root',-1)))

p1 = d['root'][0]
p2 = d['root'][2]
if solve(p2,0) != solve(p2,1):  # si p2 est la partie qui dépend de humn
	p1,p2=p2,p1
cible = solve(p2,0)				# nous devons donc atteindre cette valeur avec p1
a = 0
b = 1e20
while a < b:
	milieu = (a+b)//2
	temp = cible - solve(p1,milieu)
	if temp == 0:
		print('Partie 2 :',int(milieu))
		break
	elif temp < 0:
		a = milieu
	else:
		b = milieu