from collections import defaultdict
from os import path
from queue import Queue, PriorityQueue
from urllib.parse import ParseResult

# Read data from File .txt
def read_txt(file):
    
    size = int(file.readline().strip())
    start, goal = [int(num) for num in file.readline().strip().split()]
    
    
    matrix = []
    for line in file:
        line = line.strip()  
        if line:  
            row = [int(num) for num in line.split()]
            matrix.append(row)
    
    return size, start, goal, matrix


# Convert matrix to list
def convert_graph(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList

def convert_graph_weight(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                adjList[i].append((j, a[i][j]))
    return adjList

def BFS(graph, start, end):
    frontier = Queue()
    frontier.put(start)
    parent = {start: None}
    
    while not frontier.empty():
        current_node = frontier.get()
        
        if current_node == end:
            break
        
        for neighbor in graph[current_node]:
            if neighbor not in parent:  
                parent[neighbor] = current_node
                frontier.put(neighbor)
    
    return build_path(parent, start, end)

def DFS(graph, start, end):
    frontier = [start]
    parent = {start: None}
    
    while frontier:
        current_node = frontier.pop()
        
        if current_node == end:
            break
        
        for neighbor in graph[current_node]:
            if neighbor not in parent:
                parent[neighbor] = current_node
                frontier.append(neighbor)
    
    return build_path(parent, start, end)

   
def UCS(graph, start, end):
    frontier = PriorityQueue()
    frontier.put((0, start))
    parent = {start: None}
    cost_so_far = {start: 0}
    
    while not frontier.empty():
        current_cost, current_node = frontier.get()
        
        if current_node == end:
            break
        
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                frontier.put((new_cost, neighbor))
    
    path = build_path(parent, start, end)
    return cost_so_far.get(end, float('inf')), path

def build_path(parent, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse()
    return path if path[0] == start else []



# Output
if __name__ == "__main__":
    # Read file Input.txt and InputUCS.txt
    
    file_1 = open("C:/Users/T K/OneDrive - VNU-HCMUS/Desktop/Input.txt", "r")
    file_2 = open("C:/Users/T K/OneDrive - VNU-HCMUS/Desktop/InputUCS.txt", "r")
    size_1, start_1, goal_1, matrix_1 = read_txt(file_1)
    size_2, start_2, goal_2, matrix_2 = read_txt(file_2)
    file_1.close()
    file_2.close()
    graph_1 = convert_graph(matrix_1)
    graph_2 = convert_graph_weight(matrix_2)

    # Run BFS
     
    result_bfs = BFS(graph_1, start_1, goal_1)
    print("Result using BFS: \n", result_bfs)
    
    # Run DFS
    result_dfs = DFS(graph_1, start_1, goal_1)
    print("Result using DFS: \n", result_dfs)
    
    # run UCS
    cost, result_ucs = UCS(graph_2, start_2, goal_2)
    print("Result using UCS: \n", result_ucs, "Path Costs: ", cost)
    

          