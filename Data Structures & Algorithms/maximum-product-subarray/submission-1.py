class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxEnd=[0]*len(nums)
        minEnd=[0]*len(nums)
        maxEnd[0]=nums[0]
        minEnd[0]=nums[0]
        for i in range(1,len(nums)):
            maxEnd[i] = max(maxEnd[i-1]*nums[i],minEnd[i-1]*nums[i],nums[i])
            minEnd[i]= min(maxEnd[i-1]*nums[i],minEnd[i-1]*nums[i],nums[i])
        #print(maxEnd)
        #print(minEnd)
        return max(maxEnd)