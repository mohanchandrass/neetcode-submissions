class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        maxlen = 0

        start = [0]

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>1:
                start.append(i+1)
        
        start.append(len(nums))
        
        for i in range(len(start)-1):
            maxlen = max((start[i+1]-start[i]),maxlen)

        return maxlen