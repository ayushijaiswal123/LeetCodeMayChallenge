import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make a graph  
        pre = collections.defaultdict(list)
        for x, y in prerequisites:
            pre[x].append(y) 
        # status 0 means dont know.
        # status 1 means can take.
        # status -1 means can't take.  
        status = [0]*numCourses
        for i in range(len(status)):
            if i not in pre:
                status[i] = 1    
        def canTake(i):     
            if status[i] in {1, -1}:
                return status[i] == 1     
            status[i] = -1            
            if all([canTake(j) for j in pre[i]]):
                status[i] = 1
                return True
            else:
                status[i] = -1
                return False        
        return all([canTake(i) for i in range(numCourses)])