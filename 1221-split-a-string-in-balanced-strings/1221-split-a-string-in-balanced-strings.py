class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lst=[]
        for i in range(len(s)):
            if s[i]=='R':
                lst.append(-1)
            else:
                lst.append(1)
        pref=[lst[0]]
        res=0
        for i in range(1,len(s)):
            x=pref[-1]+lst[i]
            pref.append(x)
            if x==0 :
                res+=1
        return res