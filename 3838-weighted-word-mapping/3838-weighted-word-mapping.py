class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-97]
            res+=chr(122-(s%26))
        return res
        