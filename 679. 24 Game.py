# problem link-->> https://leetcode.com/problems/24-game/description/


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 0.000006
        def game(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24.0) <= eps
            
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if i == j:
                        continue
                    dummy = []
                    for k in range(len(arr)):
                        if k != i and k != j:
                            dummy.append(arr[k])
                    operations = [
                        arr[i] + arr[j] ,
                        arr[i] - arr[j] ,
                        arr[j] - arr[i] ,
                        arr[i] * arr[j]
                    ]
                    if arr[i] != 0:
                        operations.append(arr[j] / arr[i])
                    if arr[j] != 0:
                        operations.append(arr[i] / arr[j])
                    for op in operations:
                        if game(dummy + [op]):
                            return True
            return False

        return game(cards)
        
