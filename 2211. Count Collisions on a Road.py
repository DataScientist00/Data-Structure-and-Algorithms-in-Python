# problem link-->> https://leetcode.com/problems/count-collisions-on-a-road/description/


class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0

        directions = list(directions)
        right_going = 0
        for i in range(len(directions)-1):
            if directions[i] == 'R':
                right_going += 1
            if directions[i] == 'R' and directions[i+1] == "L":
                ans += 2
                ans += right_going -1
                right_going = 0
                directions[i+1] = 'S'
            if directions[i] == 'R' and directions[i+1] == 'S':
                ans += right_going
                right_going = 0
            if directions[i] == 'S' and directions[i+1] == "L":
                ans += 1
                directions[i+1] = 'S'
            
        return ans
            


        

