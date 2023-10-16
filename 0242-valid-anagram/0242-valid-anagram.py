class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}

        for i,ele in enumerate(s):
            d1[ele]=1+d1.get(ele,0)
        for i,ele in enumerate(t):
            d2[ele]=1+d2.get(ele,0)

        if len(s) != len(t):
            return False

        for ele in d1:
            if d1[ele]!=d2.get(ele,0):
                return False
        return True
        
        