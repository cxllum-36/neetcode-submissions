class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        q=deque()
        visit=set()
        needed=set()
        def helper(r,c):
            if (r<0 or r>=row or c<0 or c>=col or (r,c) in visit or grid[r][c]==0):
                return
            visit.add((r,c))
            q.append([r,c])
            needed.remove((r,c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c]==1:
                    needed.add((r,c))
        if len(needed)==0: return 0
        mins = -1
        while q:
            mins +=1
            for i in range(len(q)):
                r,c = q.popleft()
                print(r)
                print(c)
                helper(r+1,c)
                helper(r-1,c)
                helper(r,c+1)
                helper(r,c-1)
            
        if len(needed)!=0: return -1
        else: return mins