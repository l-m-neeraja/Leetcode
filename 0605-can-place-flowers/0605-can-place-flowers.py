class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if len(f)==1:
            if (f[0]==0 and n==1) or n==0 :
                return True
            else:
                return False
        res=0
        temp=0
        flag=0
        #
        r=0
        if f[0]==0:
            r=1
        for i in range(len(f)):
            if f[i]==1 and flag==0:
                flag=1
                if temp<=2:
                    if r and temp==2:
                        r=0
                        res+=temp//2
                    temp=0
                    continue
                else:
                    if r:
                        r=0
                        res+=temp//2
                    else:
                        res+=((temp-1)//2)
                temp=0
            elif f[i]==0:
                flag=0
                temp+=1
        if flag==0 and temp>1:
            if r:
                res+=(temp+1)//2
            else:
                res+=((temp)//2)
        print(res,temp)
        return res>=n

