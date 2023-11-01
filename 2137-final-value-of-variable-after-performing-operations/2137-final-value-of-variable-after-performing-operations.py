class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op=0
        for oper in operations:
            if oper=="++X" or oper=="X++":
                op+=1
            elif oper=="--X" or "X--":
                op-=1
        return op
