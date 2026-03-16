class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # x="".join(words)
        # mini=1000
        # for i in words:
        #     mini=min(mini,len(i))
        # if len(s)>=mini and len(s)<=len(x) and s==x[:len(s)] and len(words[0]):
        #     return True
        # return False
        res=""
        for i in words:
            res+=i
            if res==s:
                return True
        return False