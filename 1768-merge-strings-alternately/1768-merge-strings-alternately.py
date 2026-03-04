class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        mini = min(len(w1),len(w2))
        st=""
        for i in range(mini):
            st+=w1[i]
            st+=w2[i]
        if len(w1)==mini:
            for i in range(mini,len(w2)):
                st+=w2[i]
        else:
            for i in range(mini,len(w1)):
                st+=w1[i]
        return st
        