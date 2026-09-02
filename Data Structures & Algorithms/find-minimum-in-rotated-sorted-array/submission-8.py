class Solution:
    def findMin(self, nums: List[int]) -> int:
        nmin = float('inf')
        def binarysearch(nums,left,right):
            nonlocal nmin
            mid = (left+right)//2
            nmin = min(nmin,nums[left],nums[right],nums[mid])

            if left>=right:
                return 

            if nums[mid]>nums[left] or nums[left]<nums[right]:

                binarysearch(nums,left,mid-1)
            
            if nums[mid]<nums[right] or nums[left]>nums[right]:
              
                binarysearch(nums,mid+1,right)
            
            if nums[mid]>nums[left] or nums[mid]<nums[right]:
               
                binarysearch(nums,left,mid-1)
                binarysearch(nums,mid+1,right)


        binarysearch(nums,0,len(nums)-1)

        return nmin


                


        