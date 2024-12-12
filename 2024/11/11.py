with open("input.txt") as f:
	texte = f.read().strip()

def stones(i, step, obj):
	if step == obj:
		return 1
	if (i, step) in cache:
		return cache[(i,step)]
	if i == 0:
		cache[(i,step)] = stones(1, step+1, obj)
	elif len(str(i))%2==0:
		n = len(str(i))
		a = int(str(i)[:n//2])
		b = int(str(i)[n//2:])
		cache[(i,step)] = stones(a,step+1,obj) + stones(b, step+1, obj)
	else:
		cache[(i,step)] = stones(i*2024, step+1, obj)
	return cache[(i,step)]

L = list(map(int,texte.split(" ")))

cache = {}
res1 = sum(stones(i,0,25) for i in L)
print("Partie 1 :",res1)

cache = {}
res2 = sum(stones(i,0,75) for i in L)
print("Partie 2 :",res2)