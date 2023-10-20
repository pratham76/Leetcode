class Solution:
    def checkRecord(self, s: str) -> bool:
        ca = 0
        la = 0
        lmax = 0
        
        for i in s:
            if i == "A":
                ca += 1
            if i == "L":
                la += 1
            else:
                lmax = max(lmax, la)
                la = 0
        
        lmax = max(lmax, la)  # Update lmax after the loop
        
        if ca >= 2 or lmax >= 3:
            return False
        return True





