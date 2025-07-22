def f(n):
    t = 0
    while n > 0:
        c = n % 10
        t += c
        n = (n - c) // 10
    return t


f = """def f(n):
t = 0
while n>0:
    c = n %10
    t += c
    n = (n-c)//10
return t
"""
print(len(f.strip()))


def g(n):
    return sum([int(d) for d in str(n)])


print(g(8273))

p = """
def g(n):
    return sum([int(d) for d in str(n)])
"""
print(len(p))
