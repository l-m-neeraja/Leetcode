class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        st=[] 
        d={']':'[','}':'{',')':'('}
        for i in s: 
            if i in d.keys() and d[i]==st[-1]: 
                maxi=max(maxi,len(st))
                st.pop()
            if i in d.values(): 
                st.append(i)
        return maxi