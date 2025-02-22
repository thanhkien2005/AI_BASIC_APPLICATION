from collections import defaultdict
from queue import Queue, PriorityQueue


class Graph:
    def __init__(self, matrix):
        self.adj_list = self.convert_graph(matrix)

    def convert_graph(self, a):
        adj_list = defaultdict(list)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    adj_list[i].append(j)
        return adj_list

    def convert_graph_weight(self, a):
        adj_list = defaultdict(list)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] != 0:
                    adj_list[i].append((j, a[i][j]))
        return adj_list


class SearchAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def build_path(self, parent, start, end):
        path = []
        while end is not None:
            path.append(end)
            end = parent[end]
        path.reverse()
        return path if path[0] == start else []


class BFS(SearchAlgorithm):
    def search(self, start, end):
        frontier = Queue()
        frontier.put(start)
        parent = {start: None}

        while not frontier.empty():
            current_node = frontier.get()

            if current_node == end:
                break

            for neighbor in self.graph.adj_list[current_node]:
                if neighbor not in parent:
                    parent[neighbor] = current_node
                    frontier.put(neighbor)

        return self.build_path(parent, start, end)


class DFS(SearchAlgorithm):
    def search(self, start, end):
        frontier = [start]
        parent = {start: None}

        while frontier:
            current_node = frontier.pop()

            if current_node == end:
                break

            for neighbor in self.graph.adj_list[current_node]:
                if neighbor not in parent:
                    parent[neighbor] = current_node
                    frontier.append(neighbor)

        return self.build_path(parent, start, end)


class UCS(SearchAlgorithm):
    def search(self, start, end):
        frontier = PriorityQueue()
        frontier.put((0, start))
        parent = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current_cost, current_node = frontier.get()

            if current_node == end:
                break

            for neighbor, weight in self.graph.adj_list[current_node]:
                new_cost = current_cost + weight
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = current_node
                    frontier.put((new_cost, neighbor))

        path = self.build_path(parent, start, end)
        return cost_so_far.get(end, float('inf')), path


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


if __name__ == "__main__":
    # Read file Input.txt and InputUCS.txt
    with open("C:/Users/T K/OneDrive - VNU-HCMUS/Desktop/Input.txt", "r") as file_1:
        size_1, start_1, goal_1, matrix_1 = read_txt(file_1)

    with open("C:/Users/T K/OneDrive - VNU-HCMUS/Desktop/InputUCS.txt", "r") as file_2:
        size_2, start_2, goal_2, matrix_2 = read_txt(file_2)

    graph_1 = Graph(matrix_1)
    graph_2 = Graph(matrix_2)
    graph_2.adj_list = graph_2.convert_graph_weight(matrix_2)  

    # Run BFS
    bfs = BFS(graph_1)
    result_bfs = bfs.search(start_1, goal_1)
    print("Result using BFS: \n", result_bfs)

    # Run DFS
    dfs = DFS(graph_1)
    result_dfs = dfs.search(start_1, goal_1)
    print("Result using DFS: \n", result_dfs)

    # Run UCS
    ucs = UCS(graph_2)
    cost, result_ucs = ucs.search(start_2, goal_2)
    print("Result using UCS: \n", result_ucs, "Path Costs: ", cost)
