class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        lst,lstt=[0]*len(mat),[0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    lst[i]+=1
                    lstt[j]+=1
        cnt=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and lst[i]==1 and lstt[j]==1:
                    cnt+=1
        return cnt