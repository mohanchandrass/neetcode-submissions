class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for i in nums:
            hmap[i] = hmap.get(i,0)+1

        sort = sorted(hmap.items(),key = lambda x:x[1],reverse=True)

        return [num for num, i in sort[:k]]
        