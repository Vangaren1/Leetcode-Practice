from typing import Optional, List


class Trie:

    def __init__(self):
        self.letterDict = defaultdict(Trie)
        self.wordEnd = False

    def insert(self, word: str) -> None:
        ptr = self
        for w in word:
            ptr = ptr.letterDict[w]
        ptr.wordEnd = True
        

    def search(self, word: str) -> bool:
        ptr = self.find(word)
        if ptr == False:
            return False
        return ptr.wordEnd

    def startsWith(self, prefix: str) -> bool:
        ptr = self.find(prefix)
        if ptr == False:
            return False
        return True
    
    def find(self, word):
        ptr = self
        for w in word:
            ptr = ptr.letterDict.get(w)
            if ptr is None:
                return False
        return ptr


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    print("Running Solution...")
