class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights)-1
        i=0
        most=0
        while j>i:
            water = min(heights[i],heights[j])*(j-i)
            if heights[i]>heights[j]:
                j-=1
            elif heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            most = max(water,most)
        return most