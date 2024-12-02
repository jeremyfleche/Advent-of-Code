with open("input.txt") as f:
	texte = f.read()

L = [list(map(int,i.split(" "))) for i in texte.strip().splitlines()]
res1 = 0
res2 = 0
for i in L:
	if all([-4<i[j]-i[j-1]<0 for j in range(1,len(i))]) or all([0<i[j]-i[j-1]<4 for j in range(1,len(i))]):
		res1 += 1
	else:
		for j in range(len(i)):
			temp = [i[k] for k in range(len(i)) if k!=j]
			if all([-4<temp[j]-temp[j-1]<0 for j in range(1,len(temp))]) or all([0<temp[j]-temp[j-1]<4 for j in range(1,len(temp))]):
				res2 += 1
				break


print("Partie 1 :", res1)
print("Partie 1 :", res1+res2)