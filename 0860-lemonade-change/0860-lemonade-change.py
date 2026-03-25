class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t=0,0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                t+=1
                if f==0:
                    return False
                else:
                    f-=1
            else:
                if t and f:
                    t-=1
                    f-=1
                elif f >=3:
                    f-=3
                else:
                    return False
        return True
