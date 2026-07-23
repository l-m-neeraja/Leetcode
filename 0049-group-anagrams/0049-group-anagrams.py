class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for i in range(len(strs)):
            ch=list(strs[i])
            ch.sort()
            ch=''.join(ch)
            if ch in d:
                d[ch].append(i)
            else:
                d[ch]=[i]
        res=[]
        for i in d.keys():
            lst=[]
            for j in range(len(d[i])):
                lst.append(strs[d[i][j]])
            res.append(lst)
        return res