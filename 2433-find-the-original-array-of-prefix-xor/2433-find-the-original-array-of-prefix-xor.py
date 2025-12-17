class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        res=[pref[0]]
        for i in range(1,len(pref)):
            x=pref[i-1]^pref[i]
            res.append(x)
        return res