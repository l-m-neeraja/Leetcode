class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx=word.index(ch)
            temp=word[:idx+1]
            return temp[::-1]+word[idx+1:]
        return word