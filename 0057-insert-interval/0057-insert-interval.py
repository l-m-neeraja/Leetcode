class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
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