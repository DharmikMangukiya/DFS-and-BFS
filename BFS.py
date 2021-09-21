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
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '0')    # function calling