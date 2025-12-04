class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0])!=r*c:
            return mat
        res=[]
        for i in range(r):
            x=[]
            for j in range(c):
                x.append(0)
            res.append(x)
        lst=[]
        for i in mat:
            for j in i:
                lst.append(j)
        k=0
        for i in range(len(res)):
            for j in range(len(res[i])):
                if k<len(lst):
                    res[i][j]=lst[k]
                    k+=1
        return res
