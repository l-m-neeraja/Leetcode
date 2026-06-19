class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        x=0
        for i in gain:
            x+=i
            if x>=maxi:
                maxi=x
        return maxi

        