class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res,cnt=0,0
        for i in costs:
            res+=i
            if res<=coins:
                cnt+=1
            else:
                break
        return cnt