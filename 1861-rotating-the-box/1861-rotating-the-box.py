class Solution(object):
    def rotateTheBox(self, box):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        mat=[]
        res=[]
        for i in box:
            lst=[]
            h,s=0,0
            l=0
            while l<len(i):
                if i[l]=='*':
                    lst=lst+['.']*s+['#']*h+['*']
                    h,s=0,0
                elif i[l]=='#':
                    h+=1
                else:
                    s+=1
                l+=1
            lst=lst+['.']*s+['#']*h
            mat.append(lst)
        for i in range(len(mat[0])):
            lst=[]
            for j in range(len(mat)-1,-1,-1):
                lst.append(mat[j][i])
            res.append(lst)
        return res
