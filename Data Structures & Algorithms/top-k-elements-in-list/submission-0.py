class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        desc=sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return [desc[j][0] for j in range(k)]