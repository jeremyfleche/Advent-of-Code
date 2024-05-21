with open("input.txt") as f:
	texte = f.read()

# texte = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""

liste = [[[k.strip().split(" ")[:len(k.strip().split(" "))-1] for k in j.strip().split(",")] for j in i.split("contain")] for i in texte.strip().split("\n")]
t = []
for i in liste:
	temp = []
	for j in i:
		for k in j:
			temp.append(k)
	t.append(temp)

def contient(bag):
	if bag == ['no', 'other'] or bag == ['shiny', 'gold']:
		return False
	else:
		for instruction in t:
			if instruction[0] == bag:
				res = False
				for i in range(1,len(instruction)):
					if instruction[i][-2:] == ['shiny', 'gold']:
						return True
					else:
						res = res | contient(instruction[i][-2:])
	return res

def nombre_sac(bag):
	for instruction in t:
		if instruction[0] == bag:
			res = 0
			for i in range(1,len(instruction)):
				try:
					res += int(instruction[i][0]) + int(instruction[i][0])*nombre_sac(instruction[i][-2:])
				except:
					pass
			break
	return res

res = 0
for instruction in t:
	if contient(instruction[0]):
		res += 1

print("Partie 1 :",res) # 9,5 sec
print("Partie 2 :",nombre_sac(['shiny', 'gold']))