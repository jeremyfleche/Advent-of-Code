with open('input.txt','r') as f:
	texte=f.read()

signal=''
for i in texte:
	if i.isalpha():
		signal+=i

def different(temp):
	d=dict()
	for i in temp:
		d[i]=1
	if len(d)==len(temp):
		return True
	return False

for i in range(4,len(signal)):
	temp=signal[i-4:i]
	if different(temp):
		print('Partie 1 :',i)
		break

for i in range(14,len(signal)):
	temp=signal[i-14:i]
	if different(temp):
		print('Partie 2 :',i)
		break