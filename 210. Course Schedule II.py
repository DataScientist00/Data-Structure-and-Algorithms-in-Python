#problem link-->> https://leetcode.com/problems/course-schedule-ii/description/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { i:[] for i in range(numCourses)}
        cycle = []
        visit = []
        output = []
        for u , v in prerequisites:
            graph[u].append(v)
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.append(node)
            for i in graph[node]:
                if dfs(i ) == False:
                    return False
            visit.append(node)
            cycle.remove(node)
            output.append(node)


        for g in graph:
            if dfs(g ) == False:
                return []
        return output

        
