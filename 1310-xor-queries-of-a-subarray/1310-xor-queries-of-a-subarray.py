class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        px=[arr[0]]
        for i in range(1,len(arr)):
            px.append(px[-1]^arr[i])
        res=[]
        for i in queries:
            if i[0]==0:
                res.append(px[i[1]])
            else:
                res.append(px[i[1]]^px[i[0]-1])
        return res