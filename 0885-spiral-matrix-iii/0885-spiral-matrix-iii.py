class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        lst=[[rStart,cStart]]
        n,m=rows,cols
        i=0
        while len(lst)<n*m:
            i+=1
            if i%2==1:
                for j in range(1,i+1):
                    x=[rStart,cStart+j]
                    if x[0]>=0 and x[1]>=0 and x[0]<n and x[1]<m:
                        lst.append(x)
                rStart,cStart=x[0],x[1]
                for j in range(1,i+1):
                    x=[rStart+j,cStart]
                    if x[0]>=0 and x[1]>=0 and x[0]<n and x[1]<m:
                        lst.append(x)
                rStart,cStart=x[0],x[1]
            else:
                for j in range(1,i+1):
                    x=[rStart,cStart-j]
                    if x[0]>=0 and x[1]>=0 and x[0]<n and x[1]<m:
                        lst.append(x)
                rStart,cStart=x[0],x[1]
                for j in range(1,i+1):
                    x=[rStart-j,cStart]
                    if x[0]>=0 and x[1]>=0 and x[0]<n and x[1]<m:
                        lst.append(x)
                rStart,cStart=x[0],x[1]
        return lst