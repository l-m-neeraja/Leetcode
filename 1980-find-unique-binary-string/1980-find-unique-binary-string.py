class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        for i in range(2**n):
            a = format(i, f'0{n}b') 
            if a not in nums:
                return a
        