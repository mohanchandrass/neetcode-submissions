class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps = ""
        for ch in s:
            if ch.isalnum():
                ps+=ch.lower()
                
        n = len(ps)
        start = 0 
        end = n-1
        while start < end:
            if (ps[start] != ps[end]):
                return False
            start+=1
            end-=1
        
        return True

    