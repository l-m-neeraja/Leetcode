class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        d=[]
        for i in range(len(code)):
            if all(c.isalnum() or c == '_' for c in code[i]) and isActive[i]!=False and businessLine[i]!="invalid" and code[i]!='':
                d.append([code[i],businessLine[i]])
        print(d)
        k=sorted(d,key = lambda item: (item[1],item[0]))
        print(k)
        lst=[]
        for i in k:
            lst.append(i[0])
        return lst