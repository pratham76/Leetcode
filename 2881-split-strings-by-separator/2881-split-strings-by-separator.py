class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new=[]
        for i in words:
            i=i.rsplit(separator)
            while(1):
                if "" in i:
                    i.remove("")
                else:
                    break
            new+=(i)
        return new