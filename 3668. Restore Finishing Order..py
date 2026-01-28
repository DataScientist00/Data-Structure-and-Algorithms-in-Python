# problem link-->> https://leetcode.com/problems/restore-finishing-order/description/

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        friends = set(friends)
        for n in order:
            if n in friends:
                ans.append(n)
        return ans
