def dfs(graph, start, goal):
    stack = [(start, [start])]  
    close = [] 
    visited = set()
    while stack:
        print("OPEN: ",end=" ")
        print(stack)
        print("close: ",end=" ")
        print(close)
        (vertex, path) = stack.pop(0)
        close.append(path)
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            temp = []
            for neighbor in graph[vertex]:
                temp.append((neighbor, path + [neighbor]))
            stack = temp + stack   
 
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

    print (dfs(graph, 'A', 'G'))