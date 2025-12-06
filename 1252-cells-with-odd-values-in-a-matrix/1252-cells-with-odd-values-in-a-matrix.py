class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        mat=[]
        for i in range(m):
            lst=[0]*n
            mat.append(lst)
        for i in indices:
            x,y=i[0],i[1]
            for i in range(m):
                mat[i][y]+=1
            for i in range(n):
                mat[x][i]+=1
        res=0
        for i in mat:
            for j in i:
                if j%2==1:
                    res+=1
        return res
