class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def robLine(houses):
            one, two = 0, 0
            for n in houses:
                temp = max(n + one, two)
                one = two
                two = temp
            return two
            
        return max(robLine(nums[:-1]),robLine(nums[1:]))