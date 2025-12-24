class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        c,x = sorted(capacity,reverse = True),sum(apple)
        i=0
        while True:
            if x<=0:
                break
            x-=c[i]
            i+=1
        return i