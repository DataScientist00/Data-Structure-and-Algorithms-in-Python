#problem link-->> https://leetcode.com/problems/car-fleet/description/


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        clubbed = [[i , j] for i ,  j in zip(position,speed)]
        stack = []
        for pos , vel in sorted(clubbed)[::-1]:
            time = (target - pos) / vel
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
