with open('input.txt','r') as f:
	texte = f.read()

t = [i.split(' ') for i in texte.strip().split('\n')]

for ligne in t:
	if len(ligne) == 3:
		ligne[1] = ligne[1][0]
	for i in range(len(ligne)):
		if ligne[i][0] == '-':
			ligne[i] = int(ligne[i])
		elif ligne[i][0] == '+':
			ligne[i] = int(ligne[i][1:])

def solve(part):
	i = 0
	d = {'a':(0 if part == 1 else 1), 'b':0}
	while i < len(t):
		if len(t[i]) == 2 and t[i][0] in ['hlf','tpl','inc']:
			commande,r = t[i]
		elif len(t[i]) == 2:
			commande, offset = t[i]
		else:
			commande,r,offset = t[i]
		if commande == 'hlf':
			d[r]//=2
			i += 1
		if commande == 'tpl':
			d[r]*=3
			i += 1
		if commande == 'inc':
			d[r] += 1
			i += 1
		if commande == 'jmp':
			i += offset
		if commande == 'jie':
			if d[r]%2==0:
				i += offset
			else:
				i += 1
		if commande == 'jio':
			if d[r] == 1:
				i += offset
			else:
				i += 1
	return d['b']

print('Partie 1 :',solve(1))
print('Partie 2 :',solve(2))