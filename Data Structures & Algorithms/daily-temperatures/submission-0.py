class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*(len(temperatures))
        if len(temperatures) ==1: return [0]
        
        for i, temp in enumerate(temperatures):
            while stack and  temp > stack[-1][1]:
                #res[i] = i-stack[-1][1]
                idx, _ =stack.pop()
                res[idx]=i-idx
            stack.append((i, temp))
        return res