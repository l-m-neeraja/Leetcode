class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        lst=[start]
        a=2
        for i in range(n-1):
            lst.append(start+a)
            a+=2
        x=lst[0]
        lst.remove(lst[0])
        for i in lst:
            x=x^i
        return x