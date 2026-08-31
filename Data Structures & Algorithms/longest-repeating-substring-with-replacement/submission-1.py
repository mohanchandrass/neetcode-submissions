class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        left = 0
        maxcount = 0
        maxlen = 0
        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right],0)+1
            maxcount = max(maxcount,hmap[s[right]])
            replacements = (right-left+1) - maxcount
            
            while replacements>k:
                hmap[s[left]] = hmap.get(s[left],0)-1
                left+=1
                replacements = (right-left+1) - maxcount
            
            maxlen = max(maxlen,right-left+1)
            
        return maxlen
        
            