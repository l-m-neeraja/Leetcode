class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        res=0
        d={'L':0,'R':0,'_':0}
        for i in moves:
            d[i]+=1
        if d['L']>=d['R']:
            moves=moves.replace('_','L')
        else:
            moves=moves.replace('_','R')
        for i in moves:
            if i=='L':
                res-=1
            else:
                res+=1
        return abs(res)