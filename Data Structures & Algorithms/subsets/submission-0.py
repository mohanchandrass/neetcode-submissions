class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        def backtrack(i,subset):
            if i == len(nums):
                sets.append(subset.copy())
                return
            
            subset.append(nums[i])
            
            backtrack(i+1,subset)

            subset.pop()

            backtrack(i+1,subset)

            return sets
        
        return backtrack(0,[])




        