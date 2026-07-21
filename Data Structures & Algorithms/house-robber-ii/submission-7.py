class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
                return max(nums)
        def cost(nums):


            a = nums[0]
            b = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                print(a,b)
                x = a
                a,b = b, max(a+nums[i],b)
                print("i =",i,"nums[i] = ",nums[i])
                print(a,b)
            
            return max(a,b)
        
        
        return max(cost(nums[:-1]),cost(nums[1:])) 
        