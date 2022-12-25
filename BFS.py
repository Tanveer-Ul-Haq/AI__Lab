
from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):
		visited = [False] * (max(self.graph) + 1)
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(1, 3)
# g.addEdge(2, 4)

s=int(input("Enter the starting node of graph : "))
Length= int(input("Enter number of edges as a loop Length : "))
for i in range(Length):
 x=int(input("Enter first Number : "))
 y=int(input("Enter second Number : "))
 g.addEdge(x, y)


print ("Following is Breadth First Traversal (starting from vertex value of s)")
g.BFS(s)

