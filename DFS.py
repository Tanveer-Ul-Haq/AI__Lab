adj_list = {
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

color = {}     # W, G, В
parent = {}
dfs_traversal_output =  []
#initialize
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None

def dfs_util(u):
    color[u] = "G"
    dfs_traversal_output.append(u)
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u]= "В"
   
    
dfs_util("A")
print (dfs_traversal_output)
print(parent)