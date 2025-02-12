#problem link-->> https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l , r = 0 , len(people)-1
        while l <= r:
            remaining = limit - people[r]
            boats += 1
            r -= 1
            if l <= r and remaining >= people[l]:
                l += 1
        return boats
