class Solution(object):
    import string
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for i in s:
            if i.isalnum():
                st.append(i.lower())
        for i in range(len(st)//2):
            if st[i]!=st[len(st)-1-i]:
                return False
        return True
