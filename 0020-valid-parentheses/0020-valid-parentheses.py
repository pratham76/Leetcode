class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='{' or i=='[' or i=='(':
                stack.append(i)
            if i=='}' and len(stack)==0 or i==']' and len(stack)==0 or i==')' and len(stack)==0:
                return False
            if i=='}' and len(stack)!=0:
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            if i==']' and len(stack)!=0:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            
            if i==')' and len(stack)!=0:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        if not len(stack)==0:
            return False
        return True


        