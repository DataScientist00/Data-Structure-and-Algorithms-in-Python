#problem link-->> https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)
        for st in sandwiches:
            if cnt[st] > 0:
                res -= 1
                cnt[st] -= 1
            else:
                return res
        return res
        
