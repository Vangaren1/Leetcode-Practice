base = 1

def comma(n):
	s = str(n)
	neg = False
	if n < 0:
		s = s[1:]
		neg = True
	r = ""
	i = 0
	for c in s[::-1]:
		if i>0 and i % 3 == 0:
			r += ','
		i += 1
		r += c
	if neg:
		r += '-'
	return r[::-1]
	


for i in range(10):
	print(comma(base))
	base *= 10