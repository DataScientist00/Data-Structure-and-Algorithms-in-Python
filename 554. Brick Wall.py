#problem link-->>> https://leetcode.com/problems/brick-wall/description/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countgap = {0 : 0}
        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countgap[total] = 1 + countgap.get(total , 0)
        return len(wall) - max(countgap.values())

        
