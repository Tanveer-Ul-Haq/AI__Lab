# BFS
from queue import Queue

graph = {
    "A":["B","C"],
    "B":["C","D","E"],
    "C":["E"],
    "D":["G"],
    "E":["D","F"],
    "F":["D","G"],
    "G":["H","I"],
    "H":["I","E"],
    "I":[]
}

visited = {}
level = {}
parent = {}

bfs_traversal = []
queue = Queue()

for node in graph.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal.append(u)
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print(bfs_traversal)


sink = "I"
path = []
while sink is not None:
    path.append(sink)
    sink = parent[sink]
path.reverse()
print(path)