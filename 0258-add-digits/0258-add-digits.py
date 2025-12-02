class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=list(str(num))
        while True:
            i=[int(k) for k in n]
            s=str(sum(i))
            if len(s)==1:
                return int(s)
            n=list(s)