from collections import defaultdict


example = {1: "a", 2: "b", 3: "c", 4: "d"}

example[1] = "a"

copyDict = example.copy()

exList = [1, 2, 3]

copyList = exList.copy()

s = "Duplicate Database Client extensions detected! Please uninstall the duplicate."

d = defaultdict(int)

for n in s:
    d[n] += 1

print(d)


for index, char in enumerate(s):
    print(f"{index} : {char}")


for index in range(len(s)):
    tmp = "{0}: {1}".format(index, s[index])
    print(tmp)
    
    
    
class ThisClass:
    def __init__(self, val):
        self.val = val

# this line
multi = """
        multiline string 
        """
        
thisSet = set()


def tmpFunc():
    return 4

a = tmpFunc

d = {}

d
