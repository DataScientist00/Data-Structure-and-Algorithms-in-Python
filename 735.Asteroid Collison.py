#problem link--->>>https://leetcode.com/problems/asteroid-collision/description/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                if abs(i) == stack[-1]:
                    stack.pop()
                    i=0
                elif abs(stack[-1]) > abs(i):
                    i=0
                else:
                    stack.pop()               
            if i:
                stack.append(i)
        return stack
            


        
