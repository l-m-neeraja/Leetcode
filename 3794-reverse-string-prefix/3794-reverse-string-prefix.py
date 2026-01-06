class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        temp=s[:k]
        return temp[::-1]+s[k:]