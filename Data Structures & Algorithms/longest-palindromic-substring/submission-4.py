class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        res=''
        def expand(l,r):
            while  l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        def comp(odd,even):
            if len(odd)>=len(even):
                return odd
            else: return even
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(comp(odd, even))>len(res):
                res=comp(odd,even)
        return res
        '''
        n=len(s)
        dp=[[None] * n for _ in range(n)]
        bestS, bestL=0,1

        for L in range(1,n+1): #substring length
            for i in range(n-L+1): #starting index of substring
                j=i+L-1 #ending index relative to current i
                if L==1:
                    dp[i][j]=True 
                elif L==2 and s[i] == s[j]:
                    dp[i][j]=True
                elif dp[i+1][j-1] == True and s[i]==s[j]:
                    dp[i][j]=True 
                else: dp[i][j] = False
                if dp[i][j]==True:
                    bestL=L
                    bestS = i
        return s[bestS:bestL+bestS]

        