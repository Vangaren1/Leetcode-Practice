e = enumerate(['a','b','c'])


def chunker(iterable, size):

	while len(iterable) > size:
		c = iterable[0:size]
		iterable = iterable[size:]
		yield c
	if len(iterable) > 0:
		yield iterable
	

for chunk in chunker(range(25), 4):
    print(list(chunk))

