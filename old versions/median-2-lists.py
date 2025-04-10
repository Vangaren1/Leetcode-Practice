import random

m = []
n = []

a = random.randint(0,100)

while len(m) < 20:
	if a not in m:
		m.append(a)
	a = random.randint(0,100) 

n = m[:10]
m = m[10:]

m.sort()
n.sort()

print(m)
print(n)

