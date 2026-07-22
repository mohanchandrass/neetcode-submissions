class Solution:
    def countSubstrings(self, s: str) -> int:
        word = s[0]
        count = 0
        def expand(left,right):
            nonlocal count
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                count+=1
        
        for i in range(0,len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return count
            

        