class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        lst=[]
        for i in ops:
            flag=0
            if len(i)>=2 or i.isnumeric():
                i=int(i)
                lst.append(i)
            elif i=='+':
                lst.append(lst[-1]+lst[-2])
            elif i=='D':
                lst.append(2*int(lst[-1]))
            elif i=='C':
                lst.pop()
        return sum(lst)