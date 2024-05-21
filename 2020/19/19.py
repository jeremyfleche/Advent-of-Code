with open("input.txt") as f:
	file = f.read()

file = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''

texte = file.strip().split("\n\n")
mots = texte[1].strip().splitlines()

d = dict()
for ligne in texte[0].splitlines():
	key = int(ligne.split(" ")[0][:-1])
	temp = ligne.split(" ")[1:]
	if temp[0][0] == '"':
		value = eval(temp[0])
	else:
		value = []
		rule = []
		for i in temp:
			if i.isdigit():
				rule.append(int(i))
			else:
				value.append(rule)
				rule = []
		if rule != []:
			value.append(rule)
	d[key] = value

def possibilite(E,rule):
	if isinstance(d[rule],str):
		if E == set():
			return {d[rule]}
		return {i+d[rule] for i in E}
	else:
		temp = set()
		for paquet in d[rule]:
			ensemble = {i for i in E}
			for nombre in paquet:
				ensemble = possibilite(ensemble, nombre)
			temp |= ensemble
		E |= temp
	return E

E = possibilite(set(),0)

print("Partie 1 :", sum(1 for mot in mots if mot in E))

#Partie 2

d[8] = [[42],[42,8]]
d[11] = [[42, 31],[42, 11, 31]]

cache = dict()

def possibilite2(E,rule):
	if isinstance(d[rule],str):
		if E == set():
			return {d[rule]}
		return {i+d[rule] for i in E}
	else:
		temp = set()
		for paquet in d[rule]:
			ensemble = {i for i in E}
			for nombre in paquet:
				if nombre not in cache:
					cache[nombre] = ensemble
					possibilite2(ensemble, nombre)
			temp |= ensemble
		E |= temp
	return E

E = possibilite2(set(),0)
print("Partie 2 :", sum(1 for mot in mots if mot in E))