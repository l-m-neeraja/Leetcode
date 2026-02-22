class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=bin(n)
        x=x[2:]
        if abs(x.index('1')-x.rindex('1'))==0:
            return 0
        lst=[]
        for i in range(len(x)):
            if x[i]=='1':
                lst.append(i)
        maxi=0
        for i in range(len(lst)-1):
            maxi=max(maxi,lst[i+1]-lst[i])
        return maxi