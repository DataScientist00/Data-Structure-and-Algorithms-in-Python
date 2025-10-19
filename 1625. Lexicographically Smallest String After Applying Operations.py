# problem link-->> https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description/


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        q = deque([s])
        visited.add(s)
        ans = s
        while q:
            temp = q.popleft()
            ans = min(ans , temp)
            t1 = temp[b:] + temp[:b]
            if t1 not in visited:
                visited.add(t1)
                q.append(t1)
            ans = min(ans , t1)
            arr = list(temp)
            for i in range(1 , len(arr) , 2):
                arr[i] = str((int(arr[i])+a) % 10)
            t2 = ''.join(arr)
            if t2 not in visited:
                q.append(t2)
                visited.add(t2)
            ans = min(ans , t2)

        return ans
        
