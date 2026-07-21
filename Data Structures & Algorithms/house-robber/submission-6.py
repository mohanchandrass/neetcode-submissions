class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        a = nums[0]
        b = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            a,b = b, max(a+nums[i],b)
        
        return max(a,b) 
        