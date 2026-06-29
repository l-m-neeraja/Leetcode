class Solution:
    def numOfStrings(self, pat: List[str], word: str) -> int:
        res=0
        for i in pat:
            if i in word:
                res+=1
        return res