class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        jump = 0
        for i in range(len(nums)):
            if i>jump:
                return False
            curr = i+nums[i]
            jump = max(curr,jump)
    
            if jump >= goal:
                return True
        
        return False

        