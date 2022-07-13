#Median in a row-wise sorted Matrix 
def median( matrix, r, c):
    s = []
    for row in matrix:
        s.extend(row)
    s.sort() 
    mid = len(s)//2 # Finding the Mid Position
    res = (s[mid]+s[~mid])/2 # Finding the Median 
    return int(res)