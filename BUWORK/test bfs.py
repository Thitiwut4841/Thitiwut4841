def BFS(graph, start, goal):
    close = []
    open = [[start]]
     
    while open:
        path = open.pop(0)
        node = path[-1]
        if node not in close:
            neighbours = graph[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                open.append(new_path)
                print("open :" ,open)
                
                if neighbour == goal:
                    print("Best path = ", *new_path)
                    return
            close.append(node)
            print("close :" ,close)
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return


if __name__ == "__main__":
     
    graph = {'A' : ['B', 'C', 'D'],
        'B' : ['E', 'F'],
        'C' : ['F', 'G'],
        'D' : ['G'],
        'H' : [],
        'I' : [],
        'E' : ['H'],
        'J' : [],
        'K' : [],
        'F' : ['H'],
        'G' : ['I', 'J', 'K']}
     
    BFS(graph, 'A', 'G')
