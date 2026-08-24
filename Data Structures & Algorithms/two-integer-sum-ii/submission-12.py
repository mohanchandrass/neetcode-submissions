class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        i = 0
        left = 0
        right = len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total == target:
                res.append(left+1)
                res.append(right+1)
                break
            if total>target:
                right-=1
            
            if total<target:
                left+=1
            
        
        return res


        
        