class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res=[0]*len(temperatures)
        lst,st=[],[]
        for i,t in enumerate(temperatures):
            lst.append([i,t])
        for i in range(len(lst)-1,-1,-1):
            while st and st[-1][1]<=lst[i][1]:
                st=st[:-1]
            if st:
                res[i]=st[-1][0]-lst[i][0]
                st.append(lst[i])
            else:
                st.append(lst[i])
        return res