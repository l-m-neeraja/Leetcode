class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if i==j:
                    continue
                if len(words[i])<=len(words[j]):
                    if words[j][-len(words[i]):len(words[j])]==words[i] and words[j][:len(words[i])]==words[i]:
                        res+=1
        return res
