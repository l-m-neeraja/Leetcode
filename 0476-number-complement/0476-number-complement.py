class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=bin(num)[2:]
        s.rstrip('0')
        s1=""
        for i in s:
            if i=='1':
                s1+='0'
            else:
                s1+='1'
        s2=0
        for i in range(len(s1)):
            s2+=(2**(len(s1)-i-1))*int(s1[i])
        return s2