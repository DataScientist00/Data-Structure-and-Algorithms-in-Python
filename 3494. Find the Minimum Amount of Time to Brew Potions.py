# problemlink-->> https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/



class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        finishtime = [0] * len(skill)
        for i in range(len(mana)):
            finishtime[0] += skill[0] * mana[i]
            for j in range(1,len(skill)):
                finishtime[j] = max(finishtime[j-1] , finishtime[j]) + (mana[i] * skill[j])

            for j in range(len(skill)-2,-1,-1):
                finishtime[j] = finishtime[j+1] - (mana[i] * skill[j+1])

        return finishtime[-1]        
