from weighted_graph import *

graph = GraphWeighted(5)

graph.add_edge(1, 2, 1.2)
graph.add_edge(2, 5, 2.3)
graph.add_edge(3, 5, 8.4)
graph.add_edge(3, 4, 0.3)
graph.add_edge(4, 5, 4.6)
graph.add_edge(1, 5, 0.1)

print("undirected graph:")
graph.print_graph()

print("dfs:")
graph.dfs_traversal(1)

print("bfs:")
graph.bfs_traversal(1)

print("Order: " + str(graph.get_order()))

print("Number of vertices: " + str(graph.get_size()))

print("has node 3:" + str(graph.has_node(3)))
print("has node 5:" + str(graph.has_node(5)))
print("has edge 3,2: " + str(graph.has_edge(3, 2)))
print("has edge 3,1: " + str(graph.has_edge(3, 1)))
print("has path 2,3 (DFS): " + str(graph.has_path_dfs(2, 3)))
print("has path 2,5 (DFS): " + str(graph.has_path_dfs(2, 5)))
print("has path 2,3 (BFS): " + str(graph.has_path_bfs(2, 3)))
print("has path 2,5 (BFS): " + str(graph.has_path_bfs(2, 5)))

graph.remove_edge(3, 4)
print("after remove edge:")
graph.print_graph()
graph.add_edge(3, 4, 20)
print("after add back edge:")
graph.print_graph()

graph.remove_node(1)
print("after remove node:")
graph.print_graph()
print()