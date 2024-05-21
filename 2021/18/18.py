with open("input.txt") as f:
	texte = f.read()

# texte = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

texte = texte.strip().splitlines()

def magnitude(s):
	if type(s) == list:
		return 3*magnitude(s[0]) + 2*magnitude(s[1])
	else:
		return int(s)

def list_to_str(s):
	res = ""
	for i in s:
		res += str(i)
	return res

def add(s1,s2):
 return ["["]+s1+[","]+s2+["]"]

def list_of_str_to_list(s):
	temp = ""
	for i in s:
		temp += str(i)
	return eval(temp)

def conversion(s):
	res = []
	temp = ""
	for i in s:
		if i.isdigit():
			temp += i
		else:
			if temp != "":
				res.append(int(temp))
				temp = ""
			if i != " ":
				res.append(i)
	return res

def locate_explode(s):
	brackets = 0
	for i in range(len(s)):
		if s[i] == "[":
			brackets += 1
		if s[i] == "]":
			brackets -= 1
		i += 1
		if brackets > 4 and isinstance(s[i],int):
			return i-1
	return 0

def explode(s):
	i = locate_explode(s)
	if i == 0:
		return s
	avant = [s[j] for j in range(i)]
	a = s[i+1]
	b = s[i+3]
	apres = [s[j] for j in range(i+5,len(s))]
	for curseur in range(len(avant)-1,-1,-1):
		if isinstance(avant[curseur],int):
			avant[curseur] += a
			break
	for curseur in range(len(apres)):
		if isinstance(apres[curseur],int):
			apres[curseur] += b
			break		
	return avant + [0] + apres

def locate_split(s):
	for i in range(len(s)):
		if isinstance(s[i],int) and s[i] > 9:
			return i
	return False

def split(s):
	i = locate_split(s)
	if i == False:
		return s
	temp = [s[i]//2,(s[i]//2+1 if s[i]%2==1 else s[i]//2)]
	res = []
	for j in s[:i] + conversion([i for i in str(temp)]) + s[i+1:]:
		res.append((int(j) if isinstance(j,int) else str(j)))
	return res

def reduce(s):
	temp = [i for i in s]
	while temp!=explode(temp) or temp!=split(temp):
		while temp!=explode(temp):
			temp = explode(temp)
		temp = split(temp)
	return temp

s = texte[0]
s = conversion(s)
for i in range(1,len(texte)):
	s = add(s,conversion(texte[i]))
	s = reduce(s)

s = list_of_str_to_list(s)
print("Partie 1 :",magnitude(s))

res = 0
for s1 in texte:
	for s2 in texte:
		if s1 != s2:
			if magnitude(list_of_str_to_list(reduce(add(conversion(s1),conversion(s2))))) > res:
				res = magnitude(list_of_str_to_list(reduce(add(conversion(s1),conversion(s2)))))

# Attendre environ 5 secondes pour le résultat
print("Partie 2 :",res)