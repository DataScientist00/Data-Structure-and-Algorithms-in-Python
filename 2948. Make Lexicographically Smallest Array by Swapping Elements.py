# problem link-->> https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        idx_to_groups = {}
        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1] > limit):
                groups.append(deque())

            groups[-1].append(n)
            idx_to_groups[n] = len(groups)-1
        ans = []
        for n in nums:
            j = idx_to_groups[n]
            ans.append(groups[j].popleft())
        return ans
        
