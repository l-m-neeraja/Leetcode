class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        lst=[]
        for i in range(1,n+1):
            lst.append(i**2)
        for i in lst:
            for j in lst:
                if i-j in lst:
                    res+=1
        return res