with open('input.txt','r') as f:
	texte=f.read()

t=[int(i) for i in texte.split()]

res=0
for i in range(1,len(t)):
	if t[i]>t[i-1]:
		res+=1

print('Partie 1 :',res)

res=0
for i in range(1,len(t)):
	if sum(t[i:i+3])>sum(t[i-1:i+2]):
		res+=1

print('Partie 2 :',res)