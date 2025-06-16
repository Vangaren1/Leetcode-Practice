from typing import Optional, List


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.keymap = {}
        self.LRU, self.MRU = Node(0, 0), Node(0, 0)
        self.LRU.right = self.MRU
        self.MRU.left = self.LRU
        
    def get(self, key: int) -> int:
        if key in self.keymap.keys():
            #update the key to be the most recently used.
            tmp = self.keymap.get(key)
            tmp.left.right = tmp.right
            tmp.right.left = tmp.left
            self.insert(tmp)
            return tmp.val
        return -1
        
    def insert(self, newVal: Node):
        self.keymap[newVal.key] = newVal
        newVal.left = self.MRU.left
        newVal.right = self.MRU
        newVal.left.right = newVal
        self.MRU.left = newVal
        
    def removeLRU(self):
        tmp = self.LRU.right
        self.keymap.pop(tmp.key)
        if self.LRU.right.right:
            self.LRU.right.right.left = self.LRU
            self.LRU.right = self.LRU.right.right
            self.size -= 1 
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.keymap.keys():
            tmp = self.keymap.get(key)
            self.get(key)
            tmp.val = value
            return
        tmp = Node(key, value)
        self.size += 1
        if self.size <= self.capacity:
            # if there's room, put the key/value pair into the 
            # dictionary and make it the most recently used item
            self.insert(tmp)
        else:
            self.removeLRU()
            self.insert(tmp)
            


if __name__ == "__main__":
    s = LRUCache(2)
    
    s.put(1,1)
    s.put(2,2)
    print(s.get(2))
    s.put(2,3)
    print(s.get(1))
    print(s.get(2))
    
    
    print("Running Solution...")
