class Solution:
    def numberOfSpecialChars(self, wor: str) -> int:
        t={}
        for i in wor:
            t[i]=1
        re=0
        x=0
        e='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        for i in range(len(e)):
            if i%2==0:
                if e[i] in t:
                    x+=1
            if i%2==1:
                if e[i] in t and x==1:
                    re+=1
                x=0
        return re