from typing import Optional, List
import string


class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                ptr.children[w] = Node()
            ptr = ptr.children[w]
        ptr.terminal = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return ptr.terminal

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for w in prefix:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return ptr != None


if __name__ == "__main__":
    prefixTree = PrefixTree()
    print(prefixTree.insert("dog"))
    print(prefixTree.search("dog"))
    print(prefixTree.search("do"))
    print(prefixTree.startsWith("do"))
    print(prefixTree.insert("do"))
    print(prefixTree.search("do"))
    print("Running Solution...")
