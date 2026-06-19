class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack=[]
        res=''
        cur=1
        maxi=0
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
        '''for i in range(1,len(s),1):
            stack=[]
            l=i-1
            r=i+1
            stack.append(s[i])
            if i-1>=0 and s[i] == s[i-1]:
                l=i-1
                r=i
                stack=[]
            if i+1 < len(s) and s[i] == s[i+1]:
                r=i+1
                l=i
                stack=[]
            while  l>=0 and r<len(s) and s[l]==s[r]:
                stack.insert(0,s[l])
                stack.append(s[r])
                cur+=1
                r+=1
                l-=1
            maxi = max(maxi,cur)
            if len(stack) > maxi: 
                res=''
                res=''.join(stack[j] for j in range(len(stack)))
            
        return res'''
        