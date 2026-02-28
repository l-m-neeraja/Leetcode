class Solution(object):
    def asteroidCollision(self, a):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[]
        for i in a:
            if not st:
                st.append(i)
            elif (st[-1]>0 and i>0) or (st[-1]<0 and i<0):
                st.append(i)
            else:
                f=0
                while st:
                    if st[-1]>0 and i<0:
                        if abs(i)>=st[-1]:
                            n=st.pop()
                            f=1
                            if abs(i)==abs(n):
                                break
                        else:
                            f=0
                            break
                    else:
                        if i>0 and st[-1]<0:
                            f=1
                            n=0
                            break
                        else:
                            break
                    # elif st[-1]<0 and i>0:
                    #     if abs(i)>abs(st[-1]):
                    #         n=st.pop()
                    #     else:
                    #         st.append(i)
                    #         n=0
                    #         break
                if f!=0 and abs(n)!=abs(i):
                    st.append(i)
        return st
                
                
            