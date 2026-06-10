from collections import Counter as c
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=len(s1)
        if len(s1)>len(s2):
            return False
        print(c(s1))
        while j <= len(s2):
            if c(s1) != c(s2[i:j]):
                i+=1
                j+=1
            else:
                return True
        return False
