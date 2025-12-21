# problems link-->> https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/




class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs) #rows
        cols = len(strs[0]) #cols
        deleted = 0

        # sorted_pair[i] means strs[i] < strs[i+1] is already guaranteed
        sorted_pair = [False] * (rows - 1)

        for c in range(cols):
            # 1) if this column violates order for any undecided pair, delete it
            bad = False
            for r in range(rows - 1):
                if not sorted_pair[r] and strs[r][c] > strs[r + 1][c]:
                    bad = True
                    break
            if bad:
                deleted += 1
                continue

            # 2) otherwise keep it and update which pairs are now decided
            for r in range(rows - 1):
                if not sorted_pair[r] and strs[r][c] < strs[r + 1][c]:
                    sorted_pair[r] = True

            # optional early exit: all pairs decided
            if all(sorted_pair):
                break

        return deleted
