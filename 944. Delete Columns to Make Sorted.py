# problem link-->> https://leetcode.com/problems/delete-columns-to-make-sorted/description/



class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                prev = strs[j-1][i]
                if prev > strs[j][i]:
                    delete += 1
                    break
        return delete

        
