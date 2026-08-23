class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        fix = 1
        for i in range(len(nums)):
            res[i]*=fix
            fix*=nums[i]
        
        fix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=fix
            fix*=nums[i]
            
            
        return res
                
                

        