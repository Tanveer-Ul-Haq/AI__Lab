from collections import defaultdict
class Graph:
 def __init__(self):
  self.graph = defaultdict(list)

 def addEdge(self, u, v):
  self.graph[u].append(v)

 def DFSUtil(self, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in self.graph[v]:
   if visited[i] == False:
    self.DFSUtil(i, visited)

 def DFS(self, v):
  visited = [False] * (len(self.graph))
  self.DFSUtil(v, visited)

g = Graph()
s=int(input("Enter the starting node of graph "))
Length= int(input("Enter number of edges as a loop Length : "))
for i in range(Length):
 x=int(input("Enter first Number : "))
 y=int(input("Enter second Number : "))
 g.addEdge(x, y)
print("Following is DFS from (starting from vertex value of s)")
g.DFS(s)
