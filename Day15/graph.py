def isConnected(graph):
    num_nodes = len(graph)
    if num_nodes == 0:
        return True
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    start_node = next(iter(graph))
    dfs(start_node)
    return len(visited) == num_nodes


def getUserInput():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v = map(int, input("Enter an edge (u v): ").split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    return graph


def main():
    graph = getUserInput()
    if isConnected(graph):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")


if __name__ == "__main__":
    main()
