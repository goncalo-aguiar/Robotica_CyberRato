
from collections import deque

INFINITY = float("inf")


class Graph:
    def __init__(self, filename):
       

        graph_edges = []
        with open(filename) as fhandle:
            for line in fhandle:
                edge_from, edge_to, cost, *_ = line.strip().split(" ")
                graph_edges.append((edge_from, edge_to, float(cost)))

        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])

        self.adjacency_list = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.adjacency_list[edge[0]].add((edge[1], edge[2]))

    def shortest_path(self, start_node, end_node):
        

        unvisited_nodes = self.nodes.copy() 

        
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        
        previous_node = {node: None for node in self.nodes}

        while unvisited_nodes:
            
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            unvisited_nodes.remove(current_node)

           
            if distance_from_start[current_node] == INFINITY:
                break

            
            for neighbor, distance in self.adjacency_list[current_node]:
                new_path = distance_from_start[current_node] + distance
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node

            if current_node == end_node:
                break # we've visited the destination node, so we're done

        
        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path, distance_from_start[end_node]