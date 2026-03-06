class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst=[0,0]
        for i in s:
            if i=='0':
                lst[0]+=1
            else:
                lst[1]+=1
        for j in range(lst[1]):
            if s[j]=='0':
                return False
        return True