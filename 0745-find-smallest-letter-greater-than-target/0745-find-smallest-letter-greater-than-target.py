class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if target != i and sorted([target, i])[1] == i:
               return i 
                
        return letters[0]