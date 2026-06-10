class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        nums.sort()
        left=0
        cons=0
        curr=0
        right=1
        if len(nums)==0:
            return cons
        while  right < len(nums):
            if nums[right]-nums[right-1]==1:
                curr+=1
                right+=1
                if curr > cons:
                    cons = curr
            elif nums[right]-nums[right-1]==0:
                right+=1
            else:
                left=right
                right+=1
                curr=0
        return cons +1
        '''
        new=set(nums)
        current=0
        tot = 0
        if len(nums)==0:
            return tot
        for num in new:
            if num-1 not in new:
                current =1
                while (num+current) in new:
                    current+=1
                tot = max(tot, current)
        return tot