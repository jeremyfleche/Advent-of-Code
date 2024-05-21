from collections import deque

with open('input.txt','r') as f:
	texte = f.read()

def solve(part):
	t = [int(i) for i in texte.split('\n') if i!='']
	if part == 2:
		t = [i*811589153 for i in t]
	t = deque(list(enumerate(t)))
	for _ in range((1 if part == 1 else 10)):
		for i in range(len(t)):
			while t[0][0]!=i:
				t.append(t.popleft())
			temp = t.popleft()
			decalage = temp[1]%len(t)
			for _ in range(decalage):
				t.append(t.popleft())
			t.append(temp)
	for i in range(len(t)):
		if t[i][1] == 0:
			break

	return t[(i+1000)%len(t)][1]+t[(i+2000)%len(t)][1]+t[(i+3000)%len(t)][1]

print('Partie 1 :',solve(1))
print('Partie 2 :',solve(2))