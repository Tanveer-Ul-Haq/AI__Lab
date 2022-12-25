
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

level={
    "5":0,
    "3":1,
    "7":1,
    "2":2,
    "4":2,
    "8":2
}

visited = set()

def dfs(visited, tree, node, levels,dest): 
    depth = 2
    
    if (node == dest):
        print(node)
        
    elif node not in visited:
        print (node)
        visited.add(node)
        
        for neighbour in tree[node]:
            if(neighbour == dest):
                if (levels[neighbour]<=depth):
                    print(neighbour)
                    break
            elif(levels[neighbour]<=depth):
                dfs(visited, tree, neighbour, levels,dest)

print("Following is the Depth-limited Search:")
dfs(visited, graph, "5", level, "4")