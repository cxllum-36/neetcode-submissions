class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            current=1
            for j in range(len(nums)):
                
                if i !=j:
                    current = current * nums[j]
                else:
                    current = current
            output.append(current)
        return output