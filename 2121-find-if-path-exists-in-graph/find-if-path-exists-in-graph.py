class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue, seen = [], set()
        queue = [source]

        while queue:
            curr_v = queue.pop(0)
            if curr_v == destination:
                return True
            
            if curr_v not in seen:
                seen.add(curr_v)
                for neighbour in graph[curr_v]:
                    queue.append(neighbour)
        
        return False




