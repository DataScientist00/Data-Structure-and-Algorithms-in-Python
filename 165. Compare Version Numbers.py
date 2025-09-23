# problem link-->> https://leetcode.com/problems/compare-version-numbers/description/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        
        tt = abs(len(version1) - len(version2))
        for i in range(tt):
            if len(version1) > len(version2):
                version2.append(0)
            else:
                version1.append(0)
        
        print(version1)
        print(version2)

        for i in range(len(version1)):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1
        return 0


        
        
