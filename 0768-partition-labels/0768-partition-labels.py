class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash={}
        for i in range(len(s)):
            hash[s[i]]=i
        end=0
        size=0
        output=[]
        for i in range(len(s)):
            size+=1
            end=max(hash[s[i]],end)
            if i==end:
                output.append(size)
                size=0
        return output

        