class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(candidates)
        
        def backtrack(start,total,subset):
            if total == target:
                result.append(subset.copy())
                return
            if total>target:
                return
            for i in range(start,len(nums)):
                if (i>start) and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1,total+nums[i],subset)
                subset.pop()

            return result
        
        return backtrack(0,0,[])