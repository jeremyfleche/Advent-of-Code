res = []
for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				if a*b*c*d == 420:
					if {a,b,c,d} not in res:
						res.append({a,b,c,d})

print(res)