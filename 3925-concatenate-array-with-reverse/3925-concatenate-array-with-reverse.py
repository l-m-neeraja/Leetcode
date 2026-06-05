class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        x=nums[::-1]
        return nums+x