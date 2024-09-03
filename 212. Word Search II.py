#problem link-->> https://leetcode.com/problems/word-search-ii/description/


class Node:
    def __init__(self):
        self.children = {}
        self.isword = ''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()
        rows = len(board)
        cols = len(board[0])
        path = set()
        res = set()
        def build_trie():
            for word in words:
                ptr = self.root
                for char in word:
                    if char not in ptr.children:
                        ptr.children[char] = Node()
                    ptr = ptr.children[char]
                ptr.isword = word
        
        def dfs(r , c , ptr):
            if ptr.isword:
                res.add(ptr.isword)
                ptr.isword = ''
            if (r,c) in path:
                return
            if ( r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in ptr.children):
                return
            path.add((r,c))
            ptr = ptr.children[board[r][c]]

            dfs(r+1 , c ,ptr)
            dfs(r , c+1 ,ptr)
            dfs(r-1 , c ,ptr)
            dfs(r , c-1 ,ptr)
            path.remove((r,c))
        build_trie()
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,self.root)
        return list(res)

