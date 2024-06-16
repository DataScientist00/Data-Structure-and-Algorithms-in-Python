#problem link----->>> https://leetcode.com/problems/reverse-words-in-a-string-iii/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left_pointer = 0
        for right_pointer in range(len(s)):
            if s[right_pointer] == " " or right_pointer == len(s)-1:
                temp_right_pointer = right_pointer - 1
                temp_left_pointer = left_pointer
                if right_pointer == len(s) - 1:
                    temp_right_pointer = right_pointer
                while temp_left_pointer < temp_right_pointer:
                    s[temp_left_pointer] , s[temp_right_pointer] = s[temp_right_pointer] , s[temp_left_pointer]
                    temp_left_pointer += 1
                    temp_right_pointer -= 1
                left_pointer = right_pointer + 1
        return "".join(s)





        
        
