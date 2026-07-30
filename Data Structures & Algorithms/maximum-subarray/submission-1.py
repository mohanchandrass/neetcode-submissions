class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = max(nums)
        curr = 0
        for i in nums:
            curr = max(i, curr+i)
            max_sum = max(max_sum,curr)
        
        return max_sum