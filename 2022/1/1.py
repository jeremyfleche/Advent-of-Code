with open('input.txt','r') as f:
	texte=f.read()

t=[[int(j) for j in i.split('\n') if j!=''] for i in texte.split('\n\n')]
print('Partie 1 :',max([sum(i) for i in t]))
liste = sorted([sum(i) for i in t])
print('Partie 2 :',sum(liste[len(liste)-3:]))