class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)) %2 != 0: return False
        mapping={'[':']','{':'}','(':')'}
        stack=[]
        for i in s:
            if i in mapping:
                stack.append(i)
            else:
                if not stack or mapping[stack[-1]] != i:
                    return False
                stack.pop()
        return len(stack) ==0