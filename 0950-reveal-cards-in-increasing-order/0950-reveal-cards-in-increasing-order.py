class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        res=[]
        for i in range(len(deck)-1,-1,-1):
            lst=res
            x=deck[i]
            if len(res)>0:
                temp=lst[-1]
            for j in range(len(lst)-1,0,-1):
                lst[j]=lst[j-1]
            if len(res)>0:
                lst[0]=temp
            res=[x]+lst
        return res