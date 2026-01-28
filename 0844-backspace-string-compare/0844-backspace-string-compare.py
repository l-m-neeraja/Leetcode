class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st,st2=[],[]
        for i in s:
            if i=='#' and len(st)>0:
                st.pop()
            elif i=='#' and len(st)==0:
                continue
            else:
                st.append(i)
        for i in t:
            if i=='#' and len(st2)>0:
                st2.pop()
            elif i=='#' and len(st2)==0:
                continue
            else:
                st2.append(i)
        return "".join(st)=="".join(st2)