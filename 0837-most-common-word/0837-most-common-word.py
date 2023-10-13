class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        symbol = "!?',;."
        for s in symbol:
            paragraph = paragraph.replace(s, " ")
        paragraph = paragraph.split()

        from collections import Counter
        lst = sorted(Counter(paragraph).items(), key=lambda e: -e[1])
        for e, _ in lst:
            if e not in banned:
                return e
                break