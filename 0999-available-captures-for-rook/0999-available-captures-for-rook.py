class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        p,res=0,0
        for i in board:
            if 'R' in i:
                x,y=board.index(i),i.index('R')
                break
        for i in range(x-1,-1,-1):
            if board[i][y]=='B':
                break
            if board[i][y]=='p':
                res+=1
                break
        for i in range(x+1,8):
            if board[i][y]=='B':
                break
            if board[i][y]=='p':
                res+=1
                break
        for i in range(y+1,8):
            if board[x][i]=='B':
                break
            if board[x][i]=='p':
                res+=1
                break
        for i in range(y-1,-1,-1):
            if board[x][i]=='B':
                break
            if board[x][i]=='p':
                res+=1
                break
        return res