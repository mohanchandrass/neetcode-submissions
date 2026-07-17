class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
       
        def backtrack(i,total,subset):
            if total == target:
                result.append(subset.copy())
                return
            if total>target:
                return
            if i == len(nums):
                return

            subset.append(nums[i])
            backtrack(i,total+nums[i],subset)
            subset.pop()
            backtrack(i+1,total,subset)
        
            
            return result
                
            
        return backtrack(0,0,[])
            


