class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)] # [0, 1, 2, 3, 4]
        self.rank = [1] * n # [1, 1, 1, 1, 1]
    
    def find(self, u):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v) -> bool:
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent == v_parent:
            return False

        if self.rank[u_parent] > self.rank[v_parent]:
            self.parent[v_parent] = u_parent
        elif self.rank[v_parent] > self.rank[u_parent]:
            self.parent[u_parent] = v_parent
        else:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n

        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u, v):
                count -= 1
        
        return count
                
        