def bfs(graph, root):

    visited = []
    queue   = []
    queue.append(root)

    while queue:
        print(queue)

        vertex = queue.pop(0)

        print(vertex)

        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)

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

    bfs(graph, 'A')
