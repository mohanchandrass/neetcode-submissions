class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        a = nums[0]
        b = max(nums[0],nums[1])

        for i in range(2,len(nums)-1):
            print(a,b)
            x = a
            a,b = b, max(a+nums[i],b)
            print("i =",i,"nums[i] = ",nums[i])
            print(a,b)

        x = max(a,b)
        print("x=",x)

        a = nums[1]
        b = max(nums[1],nums[2])
        for i in range(3,len(nums)):
            print(a,b)
            a,b = b, max(a+nums[i],b)
            print("i =",i,"nums[i] = ",nums[i])
            print(a,b)
        
        y = max(a,b) 
        print("y=",y)


        
        return max(x,y) 
        