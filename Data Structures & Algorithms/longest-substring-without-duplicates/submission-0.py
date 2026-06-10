class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()  # tracks characters currently in the window
        maxi=0

        for right in range(len(s)):
            # if s[right] is already in the window, shrink from the left
            # until the duplicate is gone
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # now s[right] is safe to add
            seen.add(s[right])
            maxi = max(maxi, right - left + 1)
        return maxi


