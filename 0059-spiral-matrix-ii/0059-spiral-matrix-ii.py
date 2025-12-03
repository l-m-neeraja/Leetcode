class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[]
        for i in range(n):
            lst=[]
            for j in range(n):
                lst.append(0)
            matrix.append(lst)
        left,top,right,bottom=0,0,n-1,n-1
        x=1
        while(left<=right and top<=bottom ):
            for i in range(left,right+1):
                matrix[top][i]=x
                x+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=x
                x+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=x
                    x+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=x
                    x+=1
                left+=1
        return matrix