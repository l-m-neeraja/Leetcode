class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        re=0
        for i in range(num1,num2+1):
            x=str(i)
            if len(x)<3:
                continue
            for j in range(1,len(x)-1):
                if x[j]>x[j-1] and x[j]>x[j+1]:
                    re+=1
                elif x[j]<x[j-1] and x[j]<x[j+1]:
                    re+=1
        return re

            