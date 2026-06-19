class Solution:



    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if ((2 > len(nums) > 1000)or (-10,000,000 > target > 10,000,000)): 
           # return False

        hmap = {}

        
        for i, num in enumerate(nums):
            j = target - num
            if (j in hmap):
                return [hmap[j],i]
            
            hmap[num] = i

                
        
        
        
        print(hmap)



            

        