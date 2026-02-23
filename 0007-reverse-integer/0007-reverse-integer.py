class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=""
        x=str(x)
        if x[0]=="-":
            res+=x[:0:-1]
            if int(res)>=2147483648 or int(res)<=-2147483648 :
                return 0
            return 0-int(res)
        res+=x[::-1]
        if int(res)>=2147483648 or int(res)<=-2147483648:
            return 0
        return int(res)