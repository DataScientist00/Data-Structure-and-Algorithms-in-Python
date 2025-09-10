#problem link-->> https://leetcode.com/problems/minimum-number-of-people-to-teach/description/


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        sad_friends = set()
        for u , v in friendships:
            if not(set(languages[u-1]) & set(languages[v-1])):
                sad_friends.add(u-1)
                sad_friends.add(v-1)

        dictionary = Counter()
        res = 0
        for node in sad_friends:
            for lang in languages[node]:
                dictionary[lang] += 1
                res = max(res , dictionary[lang])
        return len(sad_friends) - res
        
