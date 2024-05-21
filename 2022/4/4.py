with open("input.txt") as f:
	texte = f.read()

liste = [[tuple(int(k) for k in j.split("-")) for j in i.split(",")] for i in texte.strip().splitlines()]

res1 = 0
res2 = 0
for ligne in liste:
	a = ligne[0][0]
	b = ligne[0][1]
	c = ligne[1][0]
	d = ligne[1][1]
	if (a<=c<=b and a<=d<=b) or (c<=a<=d and c<=b<=d):
		res1 += 1
	if a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d:
		res2 += 1

print("Partie 1 :",res1)
print("Partie 2 :",res2)