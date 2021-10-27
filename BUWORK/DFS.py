def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neightbour in graph[node]:
            dfs(visited, graph, neightbour)

if __name__ == '__main__':

    graph = {
        'A' : ['B', 'C', 'D'],
        'B' : ['E', 'F'],
        'C' : ['F', 'G'],
        'D' : ['G'],
        'H' : [],
        'I' : [],
        'E' : ['H'],
        'J' : [],
        'K' : [],
        'F' : ['H'],
        'G' : ['I', 'J', 'K']
        }
    print(graph)
    print("Following is Breadth Firstr Traversal")

    visited = set()

    dfs(visited, graph, 'A')