#problem link-->> https://leetcode.com/problems/check-if-move-is-legal/description/

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        row , col = len(board) , len(board[0])
        directions = [[1,0] , [0,1] , [-1 ,0] , [0,-1] , [1,-1] , [-1 , 1] , [-1 , -1] , [1 , 1]]
        board[rMove][cMove] = color
        def helper(rmove , cmove , color , direc):
            dr , dc = direc
            rmove , cmove = rmove+dr , cmove+dc
            length = 1
            while 0 <= rmove < row and 0 <= cmove < col:
                length += 1
                if board[rmove][cmove] == '.': return False
                if board[rmove][cmove]  == color:
                    return length >= 3
                rmove += dr
                cmove += dc
            return False
        for dr in directions:
            if helper(rMove , cMove , color , dr):
                return True
        return False 



        
