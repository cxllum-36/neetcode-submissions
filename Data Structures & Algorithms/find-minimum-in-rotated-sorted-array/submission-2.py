class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if nums[l]<nums[r]: return nums[l]
        while l<=r:
            mid=(l+r)//2
            if nums[mid] < nums[r] and nums[mid] < nums[l]:
                r=mid
            elif nums[mid] > nums[r] and nums[mid] > nums[l]:
                l=mid
            else: return nums[r]
        
            
