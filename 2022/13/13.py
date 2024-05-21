with open('input.txt','r') as f:
	texte = f.read()

t = [[j for j in i.split('\n') if j != ''] for i in texte.split('\n\n')]

def right_order(a,b):
	if isinstance(a, int) and isinstance(b, int):
		if a < b:
			return 1
		elif a == b:
			return 0
		else:
			return -1
	elif isinstance(a, list) and isinstance(b, list):
		i=0
		while i<len(a) and i<len(b):
			temp = right_order(a[i],b[i])
			if temp == 1:
				return 1
			if temp == 0:
				pass
			if temp == -1:
				return -1
			i+=1
		if i==len(a) and i==len(b):
			return 0
		elif i<len(a) and i==len(b):
			return -1
		else:
			return 1
	elif isinstance(a, int) and isinstance(b, list):
		return right_order([a],b)
	else:
		return right_order(a,[b])

res = 0
L = [[[2]],[[6]]]
for ligne in range(len(t)):
	l1 = eval(t[ligne][0])
	l2 = eval(t[ligne][1])
	L.append(l1)
	L.append(l2)
	if right_order(l1,l2) == 1:
		res+= (ligne+1)

print('Partie 1 :',res)

for _ in range(len(L)):
	for i in range(len(L)-1):
		if right_order(L[i],L[i+1]) == -1:
			L[i],L[i+1] = L[i+1],L[i]

print('Partie 2 :',(L.index([[2]])+1)*(L.index([[6]])+1))