#problem link-->>> https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        res , temp = [] , []
        count_dict = {
            '2' : 'abc' , '3':'def' , '4':'ghi' , '5':'jkl' ,
            '6':'mno' , '7':'pqrs' ,'8' :'tuv', '9':'wxyz'
        }
        def dfs(i):
            if i == len(digits):
                res.append(''.join(temp))
                return

            for char in count_dict[digits[i]]:
                temp.append(char)
                dfs(i+1)
                temp.pop()

        dfs(0)
        return res
        
