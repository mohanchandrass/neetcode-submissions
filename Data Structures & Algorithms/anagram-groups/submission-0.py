class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}
        for i,s in enumerate(strs):
            chars = 26*[0]
            for ch in s:
                chars[ord(ch) - ord('a')] +=1
            key = tuple(chars)
            if key not in hmap:
                hmap[key] = []
 
            hmap[key].append(s)
        
        return list(hmap.values())




        

