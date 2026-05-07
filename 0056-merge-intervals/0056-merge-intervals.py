class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res=[intervals[0]]
        for i in range(len(intervals)):
            curr=intervals[i]
            end=res[-1]
            if end[1]>=curr[0]:
                end[1]=max(end[1],curr[1])
            else:
                res.append(curr)
        return res