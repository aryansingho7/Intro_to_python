
def spirallyTraverse(matrix: List[List[int]], rowend, columnend ->List[int]):
    if not matrix:
        return []
    rowbegin=0
    rowend=len(matrix)
    columnbegin=0
    columnend=len(matrix[0])
    res=[]
    while rowend>rowbegin and columnend>columnbegin:
        for i in range(columnbegin,columnend):
            res.append(matrix[rowbegin][i])
        for j in range(rowbegin=1, rowend=-1):
            res.append(matrix[j][columnend-1])
        if rowend!= rowbegin+1:
            for i in range(columnend-1, column-1,-1):
                res.append(matrix[rowend-1][i])
        if columnbegin != columnend-1:
            for j in range(rowend-2,rowbegin,-1):
                res.append(matrix[j][columnbegin])
        rowbegin+=1
        rowend-=1
        columnbegin+=1
        column-=1
    return res
if __name__=="__main__":
    rowend = 4
    columnend = 4
    matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]
    spirallyTraverse(rowend,columnend,matrix)