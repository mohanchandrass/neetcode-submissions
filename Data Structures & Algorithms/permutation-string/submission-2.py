class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        smap = {}
        for s in s1:
            smap[s] = smap.get(s,0)+1
    
        left = 0 
        right = len(s1)

        window = {}

        for s in s2[left:right]:
            window[s] = window.get(s,0)+1
        
        while right<len(s2):
            if window == smap:
                return True
            
            window[s2[left]]-=1
            if window[s2[left]] == 0:
                window.pop(s2[left])

            left+=1
            window[s2[right]] = window.get(s2[right],0)+1
            right+=1
            
        if window == smap:
            return True


        
        return False
            