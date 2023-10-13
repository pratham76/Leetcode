class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash=Counter(stones)
        count=0
        for i in jewels:
            if hash[i]:
                count+=hash[i]
        return count
        