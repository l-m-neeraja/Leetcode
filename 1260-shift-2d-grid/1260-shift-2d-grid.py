class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        for i in grid:
            for j in i:
                lst.append(j)
        k=k%(len(lst))
        temp=lst[len(lst)-k:]+lst[:len(lst)-k]
        k=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]=temp[k]
                k+=1
        return grid