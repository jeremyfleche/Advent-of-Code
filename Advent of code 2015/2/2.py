with open('input.txt','r') as f:
	texte = f.read()

t = [[int(j) for j in i.split('x')] for i in texte.strip().split('\n')]

res = 0
for i in t:
	l,w,h = i
	res += 2*l*w + 2*w*h + 2*l*h + sorted(i)[0]*sorted(i)[1]

print('Partie 1 :',res)

#Partie 2

res = 0
for i in t:
	l,w,h = i
	res += l*w*h + 2*sorted(i)[0]+2*sorted(i)[1]

print('Partie 2 :',res)