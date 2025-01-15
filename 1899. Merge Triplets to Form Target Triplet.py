#problem link-->> https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pos = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i , p in enumerate(t):
                if p == target[i]:
                    pos.add(i)
        return len(pos) == 3 
        
