class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        a=0
        res=0
        while True:
            if len(word)//8==0:
                a+=1
                res+=(len(word))*a
                break
            else:
                a+=1
                res+=8*a
                word=word[:len(word)-8]
        return res
