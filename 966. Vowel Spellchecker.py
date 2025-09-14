# problem link-->> https://leetcode.com/problems/vowel-spellchecker/description/



class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        capwords= {}
        asterick = {}
        exact = set(wordlist)
        for w in wordlist:
            if w.lower() not in capwords:
                capwords[w.lower()] = w
            ss = ''
            for c in w.lower():
                if c in 'aeiou':
                    ss += '*'
                else:
                    ss += c
            if ss not in asterick:
                asterick[ss] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            elif q.lower() in capwords:
                ans.append(capwords[q.lower()])
                continue
            else:
                ss = ''
                for c in q.lower():
                    if c in 'aeiou':
                        ss += '*'
                    else:
                        ss += c
                if ss in asterick:
                    ans.append(asterick[ss])
                else:
                    ans.append('')
        return ans
            
        
