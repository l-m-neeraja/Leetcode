class Solution:
    def triangularSum(self, lst: List[int]) -> int:
        while len(lst)>1:
            temp=[]
            for i in range(1,len(lst)):
                temp.append((lst[i]+lst[i-1])%10)
            lst=temp
        return lst[0]