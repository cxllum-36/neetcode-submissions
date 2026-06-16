class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        if l < 100: n=1
        elif 100 <= l < 1000: n=10
        else: n = 100
        for i in range(len(nums)):
            if nums[i]==target: return i
        return -1