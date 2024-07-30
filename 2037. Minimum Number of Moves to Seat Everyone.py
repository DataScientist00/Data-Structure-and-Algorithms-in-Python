#problem link-->> https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res =0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            if seats[i] != students[i]:
                res = res + abs(seats[i]- students[i])
        return res
        
