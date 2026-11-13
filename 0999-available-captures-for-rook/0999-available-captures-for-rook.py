class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        def rook_position(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]=='R':
                        return [i,j]
        r,c=rook_position(board)
        self.ans=0
        def isSafe(r,c):
            if r>=0 and c>=0 and r<len(board) and c<len(board[0]):
                return True
            else:
                return False
        def top_down(board):
            for i in range(r,-1,-1):
                if board[i][c]=='B':
                    break
                elif board[i][c]=='p':
                    self.ans+=1
                    break
            for i in range(r,len(board)):
                if board[i][c]=='B':
                    break
                elif board[i][c]=='p':
                    self.ans+=1
                    break
            for i in range(c,-1,-1):
                if board[r][i]=='B':
                    break
                elif board[r][i]=='p':
                    self.ans+=1
                    break
            for i in range(c,len(board[0])):
                if board[r][i]=='B':
                    break
                elif board[r][i]=='p':
                    self.ans+=1
                    break
        top_down(board)
        return self.ans