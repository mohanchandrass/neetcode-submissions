class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        res = []

        for i in nums:
            hmap[i] = hmap.get(i,0)+1

        sort = sorted(hmap.items(),key = lambda x:x[1],reverse=True)

        for i in range(k):
            res.append(sort[i][0])

        return res
        