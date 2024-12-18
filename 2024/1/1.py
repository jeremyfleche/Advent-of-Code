with open("input.txt") as f:
	texte = f.read().splitlines()

L = [i.split(" ") for i in texte]
a = [int(i[0]) for i in L]
b = [int(i[-1]) for i in L]

c = list(sorted(a))
d = list(sorted(b))

res1 = sum(abs(c[i]-d[i]) for i in range(len(c)))
print("Partie 1 :", res1)

d = {}
for i in b:
	d[i] = d[i]+1 if i in d else 1

res2 = 0
for i in a:
	res2 += i*d[i] if i in d else 0

print("Partie 2 :", res2)