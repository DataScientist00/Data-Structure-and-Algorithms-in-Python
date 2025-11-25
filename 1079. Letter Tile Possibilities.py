# problem link-->> https://leetcode.com/problems/letter-tile-possibilities/description/


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        used = set()

        def dfs(path):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                if i in used:
                    continue
                used.add(i)
                dfs(path + tiles[i])
                used.remove(i)

        dfs("")
        return len(res)

        
