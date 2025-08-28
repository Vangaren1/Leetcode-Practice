from typing import Optional, List
import string


class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                ptr.children[w] = Node()
            ptr = ptr.children[w]
        ptr.terminal = True

    def search(self, word: str) -> bool:
        ptr = self.root
        return self._find(word, ptr)

    def _find(self, word, ptr):
        for index, w in enumerate(word):
            if w != "." and w not in ptr.children:
                return False
            if w == ".":
                remainingWord = word[index + 1 :]
                return any(
                    [self._find(remainingWord, p) for p in ptr.children.values()]
                )
            ptr = ptr.children[w]
        return ptr.terminal


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")
    wordDictionary.search("say")
    wordDictionary.search("day")
    wordDictionary.search(".ay")
    wordDictionary.search("b..")
    print("Running Solution...")
