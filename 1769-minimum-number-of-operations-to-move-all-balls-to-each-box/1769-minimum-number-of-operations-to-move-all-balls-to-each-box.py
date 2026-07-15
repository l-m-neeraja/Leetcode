class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                lst.append(i)
        res=[]
        for i in range(len(boxes)):
            x=0
            for j in lst:
                x+=(abs(i-j))
            res.append(x)
        return res