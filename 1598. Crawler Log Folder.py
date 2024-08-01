#problem link--->>> https://leetcode.com/problems/crawler-log-folder/description/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for temp in logs:
            if temp == "../":
                if counter > 0:
                    counter -= 1

            elif temp != "./":
                counter +=1
        return counter


        
        
