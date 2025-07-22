from typing import Optional, List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class trie:
            def __init__(self, array: list):
                self.curr = array.pop(0)
                self.tDict = {}
                self.terminating = len(array) == 0

                ptr = self.tDict
                if array:
                    tmp = trie(array)
                    self.tDict[tmp.curr] = tmp

        thisTrie = trie([None])

        for fold in folder:
            array = fold.split("/")
            array.pop(0)
            tmp = trie(array)
            thisTrie.tDict[tmp.curr] = tmp


if __name__ == "__main__":
    s = Solution()

    folder = ["/ap/ax/ay", "/ap/aq/au", "/aa/ab/af", "/aa/ai/am", "/ap/ax", "/ap/aq/ar"]
    expected = ["/a", "/c/d", "/c/f"]

    print(s.removeSubfolders(folder))
    print("Running Solution...")
