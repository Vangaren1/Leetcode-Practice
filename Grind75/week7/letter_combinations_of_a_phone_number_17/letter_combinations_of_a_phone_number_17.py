from typing import Optional, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        results = []
        
        while digits: 
            currDigit = digits[0]
            digits = digits[1:]
            if len(results) == 0:
                results = [ s for s in letters.get(currDigit)]
            else:
                for tmp in results.copy():
                    results.remove(tmp)
                    for curr in letters.get(currDigit):
                        results.append(tmp+curr)
        
        return results

if __name__ == "__main__":
    print("Running Solution...")
