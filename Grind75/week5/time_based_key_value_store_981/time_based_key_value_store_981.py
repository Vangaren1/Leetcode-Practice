from typing import Optional, List

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.timeBasedDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort_right( self.timeBasedDict[key], (timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        tmp = self.timeBasedDict.get(key)
        if not tmp:
            return ""
        index = bisect.bisect_right(tmp, (timestamp, chr(255)))
        if index == 0:
            return ""
        return tmp[index -1][1]
        
        

      

if __name__ == "__main__":
    t = TimeMap()
    
    t.set('foo', 'bar', 1)

    print(t.get('foo', 1))
    print(t.get('foo', 3))
    t.set("foo", "bar2", 4)
    print(t.get("foo", 4))
    
    
    print("Running Solution...")
