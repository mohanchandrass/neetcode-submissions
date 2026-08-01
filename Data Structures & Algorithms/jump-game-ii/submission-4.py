class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        jump = 0
        count = 0
        maxreach = 0
        if jump>=goal:
            return count
        for i in range(len(nums)):
            curr = i + nums[i]
            maxreach = max(curr,maxreach)
            if i == jump:
                count+=1
                jump = maxreach
            if jump>=goal:
                return count
        
        return count


        