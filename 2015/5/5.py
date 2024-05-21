fichier=open('input.txt')
texte=fichier.read()
fichier.close()

mot=''
t=[]
for i in texte:
	if i=='\n':
		t.append(mot)
		mot=''
	else:
		mot+=i


def condition1(s):
	voyelles='aeiou'
	counter=0
	for i in s:
		if i in voyelles:
			counter+=1
	if counter>=3:
		return True
	return False


def condition2(s):
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			return True
	return False


def condition3(s):
	liste=['ab','cd','pq','xy']
	for i in range(len(s)-1):
		if s[i:i+2] in liste:
			return False
	return True


counter=0
for i in t:
	if condition1(i) and condition2(i) and condition3(i):
		counter+=1

print(counter)

#Partie 2

def condition4(s):
	for i in range(len(s)-1):
		for j in range(len(s)-1):
			if s[i:i+2]==s[j:j+2] and i!=j+1 and i!=j-1 and i!=j:
				return True
	return False


def condition5(s):
	for i in range(len(s)-2):
		if s[i]==s[i+2] and s[i]!=s[i+1]:
			return True
	return False

counter=0
for i in t:
	if condition4(i) and condition5(i):
		counter+=1

print(counter)