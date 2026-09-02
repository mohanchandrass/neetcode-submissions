class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarysearch(nums,left,right):

            if left>=right:
                return left
            
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                return binarysearch(nums,mid+1,right)
            
            else:     
                return binarysearch(nums,left,mid)
            


        return nums[binarysearch(nums,0,len(nums)-1)]


