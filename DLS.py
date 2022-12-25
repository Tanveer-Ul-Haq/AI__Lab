from collections import defaultdict
class Graph:
 def __init__(self):
  self.graph = defaultdict(list)

 def addEdge(self, u, v):
  self.graph[u].append(v)

 def DLSUtil(self, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in self.graph[v]:
   if visited[i] == False:
    self.DLSUtil(i, visited)

 def DLS(self, v):
  visited = [False] * (len(self.graph))
  self.DLSUtil(v, visited)

g = Graph()
Length= int(input("Enter number of edges as a loop Length : "))
for i in range(Length):
 x=int(input("Enter first Number : "))
 y=int(input("Enter second Number : "))
 g.addEdge(x, y)
s=int(input("Enter the starting node of graph "))
dest=int(input("Enter Destination node: "))
depth=int(input("Enter Depth value: "))

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

print("Following is DLS from (starting from vertex value of s)")
g.DLS(s)
