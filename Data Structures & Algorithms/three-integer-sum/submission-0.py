class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        sols = set()
        for i in range(len(s)):
            k=len(s)-1
            j=i+1
            while j < k:
                if s[j]+s[k]>-s[i]:
                    k-=1
                elif s[j]+s[k]<-s[i]:
                    j+=1
                else:
                    sols.add((s[i], s[j], s[k]))
                    k-=1
        return list(sols)