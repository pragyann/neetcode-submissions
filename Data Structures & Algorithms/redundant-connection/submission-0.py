class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)  # {v: [edges]}

        def path_exists(u, v):
            stack = [u]
            visited = set()
            visited.add(u)
            
            while stack:
                node = stack.pop()

                for nei in adj_list[node]:
                    if nei == v:
                        return True
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            
            return False

        for u, v in edges:
            if path_exists(u, v):
                return [u, v]
            
            adj_list[u].append(v)
            adj_list[v].append(u)
        

