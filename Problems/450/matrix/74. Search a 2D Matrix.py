class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix: return False
        N=len(matrix[0])
        M=len(matrix)
        l,r=0, (N*M)-1
        
        while l<r:
            mid=(l+r)//2
            if matrix[mid//N][mid%N]==target:
                return True
            elif matrix[mid//N][mid%N]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        
    