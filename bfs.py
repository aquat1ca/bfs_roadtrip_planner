#depth first search
from collections import deque

graph = {
    'LA':["Phonex"],
    'Phonex':['El Peso'],
    'El Peso':['Dallas', 'Houston'],
    'Houston':['New Orleans'],
    'Dallas':["Little rock"],
    'Little rock':['New Orleans'],
    'New Orleans':[]
}

# follower_graph={
#     "Mo":["Kate"],
#     "Kate":["Taylor","Sam"],
#     "Sam":["Kate", "Taylor"],
#     "Taylor":["Trump"],
#     "Trump":[]
# }

#this is a breadth first search function
#@graph: the graph to traverse
#@start: start node
#@goal: goal node
def BFS_v1(graph, start, goal):
    queue = deque([start]) #my to do list starts with the start node
    while queue: #while I can still go to some node in the queue
        current_node = queue.popleft() #popleft gets the first node in the queue, FIFO
        print(current_node)
        if current_node == goal:
            print("I found the goal!")
            return
        
        #append all the neighbor nodes to the queue
        for node in graph[current_node]:
            queue.append(node)
    
    print("I cannot find the goal!")
    return

# ----- BFS Function -----
def bfs_path(graph, start, goal):
    queue = deque([start])
    visited = set()
    parent = {}

    while queue:
        current = queue.popleft()
        visited.add(current)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current
    return None