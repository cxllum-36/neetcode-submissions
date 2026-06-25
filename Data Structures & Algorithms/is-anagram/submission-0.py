class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        j=Counter(s)
        k=Counter(t)
        
        if j==k: return True
        else: return False