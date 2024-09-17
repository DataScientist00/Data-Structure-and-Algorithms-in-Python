#problem link-->> https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if cycle detects then we can't finish all courses
        visited = set()
        graph = { i:[] for i in range(numCourses)}
        for u , v in prerequisites:
            graph[u].append(v)
        def dfs(u):
            if u in visited:
                return False
            if graph[u] == []:
                return True
            visited.add(u)
            for node in graph[u]:
                if not dfs(node): return False
            visited.remove(u) #it can be safely removed from the current path 
                                #and be allowed to appear again in different paths.
            graph[u]=[] #this helps to avoid redundant DFS calls in the future
            return True
        for n in graph:
            if not dfs(n): return False
        return True

        

        
