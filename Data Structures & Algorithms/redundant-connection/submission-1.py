class DSU:
    def __init__(self, count: int):
        self.parent = [i for i in range(count + 1)] # [0, 1, 2, 3, 4]
        self.rank = [1] * (count + 1) # [1, 1, 1, 1, 1]
    
    def find(self, x) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

        # if (x = self.parent[x]):
        #     return x

        # self.parent[x] = find(self.parent[x])
        # return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += self.rank[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += self.rank[x_parent]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if dsu.find(u) == dsu.find(v):
                return [u,v]
            
            dsu.union(u, v)
