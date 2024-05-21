with open('input.txt','r') as f:
	texte = f.read()

t = texte.strip().split('\n')

def base5_to_dec(nombre):
	res = 0
	d = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
	for i in range(len(nombre)):
		res += (d[nombre[i]]*5**(len(nombre)-1-i))
	return res

def dec_to_base5(nombre):
	res = ''
	x = nombre
	d = {2:'2',1:'1',0:'0',-1:'-',-2:'='}
	while x != 0:
		q = x // 5
		r = x-5*q
		if r>2:
			q += 1
			r -= 5
		res += d[r]
		x = q
	return res[::-1]

res = 0
for nombre in t:
	res += base5_to_dec(nombre)

print('Réponse :',dec_to_base5(res))