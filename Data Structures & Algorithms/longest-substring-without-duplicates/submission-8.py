class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxcount = 0
        count = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])    
                left+=1
                count-=1
            
            seen.add(s[right])
            count+=1
            
            maxcount = max(count,maxcount)

            
            
        return maxcount