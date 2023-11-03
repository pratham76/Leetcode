class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        def ispal(a):
            return a==a[::-1]
                

        longest=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substr=s[i:j]
                if ispal(substr) and len(substr)>len(longest):
                    longest=substr
        return longest
        """
        res=""
        longpal=0

        for i in range(len(s)):
            #oddlen
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>longpal:
                    res=s[l:r+1]
                    longpal=r-l+1
                r+=1
                l-=1
            #evenlen
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>longpal:
                    res=s[l:r+1]
                    longpal=r-l+1
                r+=1
                l-=1
        
        return res
            
                    

        