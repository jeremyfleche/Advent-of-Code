with open("input.txt") as f:
	texte = f.read().strip()

t = texte.splitlines()
operations = [[int(i.split(':')[0]), list(map(int, [j for j in i.split(':')[1].strip().split(" ")]))] for i in t]

def correct1(result, operands):
	Q = [operands[0]]
	for i in range(1, len(operands)):
		new_Q = []
		while Q:
			temp = Q.pop()
			if temp > result:
				continue
			new_Q.append(temp+operands[i])
			new_Q.append(temp*operands[i])
		Q = [i for i in new_Q]
	return result in Q

def correct2(result, operands):
	Q = [operands[0]]
	for i in range(1, len(operands)):
		new_Q = []
		while Q:
			temp = Q.pop()
			if temp > result:
				continue
			new_Q.append(temp+operands[i])
			new_Q.append(temp*operands[i])
			new_Q.append(int(str(temp)+str(operands[i])))
		Q = [i for i in new_Q]
	return result in Q

res1 = sum(result for (result, operands) in operations if correct1(result, operands))
res2 = sum(result for (result, operands) in operations if correct2(result, operands))

print("Partie 1 :", res1)
print("Partie 2 :", res2)