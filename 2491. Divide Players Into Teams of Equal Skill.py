# problem link-->> https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)//2
        skill.sort()
        target = skill[0] + skill[-1]
        l = 0
        r = len(skill)-1
        ans = 0
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            ans += (skill[l] * skill[r])
            l += 1
            r -= 1
        return ans
        

        
