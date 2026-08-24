class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total == target:
                break
            if total>target:
                right-=1
            
            if total<target:
                left+=1
            
        
        return [left+1,right+1]


        
        