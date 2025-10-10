# problem link-->> https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -1001
        n = len(energy)
        for i in range(len(energy)-1,-1,-1):
            if i+k < n:
                energy[i] = energy[i] + energy[i+k]
            ans = max(ans , energy[i])
        return ans              
        
