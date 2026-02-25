class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in arr:
            x=bin(i).replace("0", "")
            lst.append([len(x),i])
        lst.sort()
        res=[]
        for i in lst:
            res.append(i[1])
        return res
