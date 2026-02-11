class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxi=-1
        cnt=0
        for i in range(k):
            if s[i] in ['a','e','u','i','o']:
                cnt+=1
        maxi=max(maxi,cnt)
        for i in range(k,len(s)):
            if s[i-k] in ['a','e','u','i','o']:
                cnt-=1
            if s[i] in ['a','e','u','i','o']:
                cnt+=1
            maxi=max(maxi,cnt)
        return maxi