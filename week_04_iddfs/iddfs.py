# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': []

}

def depth_limited_dfs(graph, current_node, goal_node, depth_limit):
    if current_node == goal_node:
        print(f"Goal found at depth {depth_limit}")
        return True

    if depth_limit == 0:
        return False

    for neighbor in graph.get(current_node, []):
        if depth_limited_dfs(graph, neighbor, goal_node, depth_limit - 1):
            return True

    return False

def iterative_deepening_dfs(graph, start_node, goal_node):
    depth = 0
    while True:
        print(f"Searching with depth limit: {depth}")
        if depth_limited_dfs(graph, start_node, goal_node, depth):
            print("Search successful!")
            return True
        
        depth += 1

# Example Usage
start_node = 'A'
goal_node = 'K'
iterative_deepening_dfs(graph, start_node, goal_node)
