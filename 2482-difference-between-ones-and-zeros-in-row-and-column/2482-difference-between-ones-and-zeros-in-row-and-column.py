class Solution(object):
    def onesMinusZeros(self, mat):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        lst1,lstt1=[0]*len(mat),[0]*len(mat[0])
        lst0,lstt0=[0]*len(mat),[0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    lst1[i]+=1
                    lstt1[j]+=1
                else:
                    lst0[i]+=1
                    lstt0[j]+=1
        res=[[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[i][j]=lst1[i]+lstt1[j]-lst0[i]-lstt0[j]
        return res