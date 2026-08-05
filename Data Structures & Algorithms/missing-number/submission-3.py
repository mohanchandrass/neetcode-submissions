class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = 0
        while i<len(nums):
            n^=i^nums[i]
            i+=1

        
        return n^i
    
     

        