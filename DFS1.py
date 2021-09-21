graph = {
  '0' : ['1','2'],
  '1' : ['5', '6'],
  '6' : ['7'],
  '2' : ['3','4'],
  '3' : ['8'],
  '8' : [],
  '7' : [],
  '5' : [],
  '4' : []

}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '0')