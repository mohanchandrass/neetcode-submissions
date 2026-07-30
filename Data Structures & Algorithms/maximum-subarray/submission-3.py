class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = nums[0]
        for i in nums[1:]:
            curr = max(i, curr+i)
            max_sum = max(max_sum,curr)
        
        return max_sum