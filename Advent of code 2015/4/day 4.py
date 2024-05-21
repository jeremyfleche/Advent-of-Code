import hashlib

cle='ckczppom'

counter=1
mot=cle+str(counter)
while hashlib.md5(mot.encode('utf-8')).hexdigest()[0:6]!='000000':
	counter+=1
	mot=cle+str(counter)

print(counter)