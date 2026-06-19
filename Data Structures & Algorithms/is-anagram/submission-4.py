class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if((len(s)!=len(t)) or (1 > len(s) >5 * 10^4) or (1> len(t) > 5 * 10^4)):
            return False
    
        count = {}
        for i in s:
            count[i] = count.get(i,0)+1
        for i in t:
            count[i] = count.get(i,0)-1
        
        for values in count.values():
            if values != 0:
                return False
                
        
        return True

            
    