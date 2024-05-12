with open("input.txt") as f:
	texte = f.read()

# texte = """px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}"""

a, b = texte.strip().split('\n\n')

d = dict()
for ligne in a.splitlines():
	(key, temp) = ligne[:-1].split("{")
	d[key] = [i.split(':') for i in temp.split(',')]
		

valeurs = []
for ligne in b.splitlines():
	liste = []
	temp = ""
	for i in ligne:
		if i.isdigit():
			temp += i
		elif temp != "":
			liste.append(int(temp))
			temp = ""
	if temp != "":
		liste.append(int(temp))
	valeurs.append(liste)

res = 0
for x,m,a,s in valeurs:
	current = 'in'
	while current not in ('A','R'):
		for condition in d[current]:
			if len(condition) == 2:
				p, q = condition
				if eval(p):
					current = q
					break
			else:
				current = condition[0]
	if current == 'A':
		res += x+m+a+s

print("Partie 1 :",res)

def solve(liste,current):
	res = 0
	x,m,a,s = liste
	if current == 'A':
		return (x[1]-x[0]) * (m[1]-m[0]) * (a[1]-a[0]) * (s[1]-s[0])
	if current == 'R':
		return 0
	for condition in d[current]:
		if len(condition) == 2:
			p, q = condition
			if '<' in p:
				variable, value = p.split('<')
				value = int(value)
				if variable == 'x':
					res += solve([(x[0],value),m,a,s],q)
					x = (value, x[1])
				elif variable == 'm':
					res += solve([x,(m[0],value),a,s],q)
					m = (value, m[1])
				elif variable == 'a':
					res += solve([x,m,(a[0],value),s],q)				
					a = (value, a[1])
				else:
					res += solve([x,m,a,(s[0],value)],q)
					s = (value, s[1])
			else:
				variable, value = p.split('>')
				value = int(value)
				if variable == 'x':
					res += solve([(value+1,x[1]),m,a,s],q)
					x = (x[0],value+1)
				elif variable == 'm':
					res += solve([x,(value+1,m[1]),a,s],q)
					m = (m[0],value+1)
				elif variable == 'a':
					res += solve([x,m,(value+1,a[1]),s],q)				
					a = (a[0],value+1)
				else:
					res += solve([x,m,a,(value+1,s[1])],q)
					s = (s[0],value+1)
		else:
			res += solve([x,m,a,s],condition[0])

	return res


liste = [(1,4001) for _ in range(4)]
print("Partie 2 :",solve(liste,'in'))