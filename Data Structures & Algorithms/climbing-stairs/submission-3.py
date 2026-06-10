class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[1,2]
        i=2
        if n ==2:
            return 2
        if n ==1:
            return 1
        while i < n:
            count=arr[i-1]+arr[i-2]
            arr.append(count)
            
            i+=1

        return arr[n-1]