def dfs(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    time_in = [0] * n
    time_out = [0] * n
    timer = 0
    
    def dfs_recursive(v):
        nonlocal timer
        visited[v] = True
        time_in[v] = timer
        timer += 1
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs_recursive(neighbor)
        
        time_out[v] = timer
        timer += 1
    
    dfs_recursive(start_vertex)
    return time_in, time_out