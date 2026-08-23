class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix = [1]*len(nums)
        prefix[0] = 1
        suffix = [1]*len(nums)
        suffix[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]

            
            
        return res
                
                

        