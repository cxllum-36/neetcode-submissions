class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        
        def search(matrix,target, start,end):
            while start<=end:
                mid = (start+end)//2

                if matrix[mid][0]<=target<=matrix[mid][-1]: return mid
                if matrix[mid][0] > target:
                    end = mid-1
                else:
                    start = mid+1
            return mid 
        row = search(matrix,target,top,bottom)
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]==target: return True
            if matrix[row][mid] > target:
                    right = mid-1
            else:
                left = mid +1
        return False