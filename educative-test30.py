from collections import defaultdict

def dfs(adj_map, target, time_left, root_node, prob) -> float:
   # Handle the leaf node or time - elapsed
    if time_left == 0 or len(adj_map[root_node]) == 0:
       if target == root_node:
           return 1/prob
       else:
           return 0.0 
        
    # For internal nodes perform the dfs on the child node
    new_prob = prob * len(adj_map[root_node])
    time_left -= 1
    res_prob = 0.0
    for node in adj_map[root_node]:
        res_prob = max(res_prob, dfs(adj_map, target, time_left, node, new_prob))

    return res_prob

def frogPosition(n, edges, t, target):
    adj_map = defaultdict(list)
    adj_map[1] = []

    adj_map2 = defaultdict(list)
    adj_map2[1] = []

    for u,v in edges:
        adj_map[u].append(v)
    if len(adj_map[1]) > 0:    
        return dfs(adj_map, target, t, 1, 1.0)
    
    # Inverted Tree: Travese in other direction of edges v->u
    adj_map.clear()
    for u,v in edges:
        adj_map[u].append(v)
    return dfs(adj_map, target, t, 1, 1.0)  

'''
       4, [[1, 2], [2, 3], [3, 4]],4,4
       6, [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]],2,6
       4, [[1, 2], [1, 3], [2, 4]],2,2
       5, [[1, 2], [1, 3], [3, 4], [4, 5]],2,5
       3, [[1, 2], [1, 3]],0,1
'''

def frogPosition_sol(n, edges, t, target):
    # Build adjacency list for the undirected tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS queue holds tuples: (current_node, current_probability)
    q = deque([(1, 1.0)])
    # Track visited to avoid revisiting nodes (frog can't go back)
    visited = [False] * (n + 1)
    visited[1] = True
    
    # Each loop iteration consumes one second
    time_left = t
    while q and time_left >= 0:
        # All items currently in the queue correspond to this exact second
        level_size = len(q)
    
        for _ in range(level_size):
            u, p = q.popleft()
    
            # Count unvisited neighbors of u (the only places the frog can jump next)
            cnt_unvisited = 0
            for v in graph[u]:
                if not visited[v]:
                    cnt_unvisited += 1
    
            # If we're at target: either we must stay or must leave
            if u == target:
                # If time is up OR there are no unvisited neighbors (we'll stay),
                # return the current probability.
                if time_left == 0 or cnt_unvisited == 0:
                    return p
                # Otherwise, the frog must leave before time runs out → prob 0.
                return 0.0
    
            # Push unvisited neighbors with split probability
            if cnt_unvisited > 0:
                split = p / cnt_unvisited
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append((v, split))
    
        time_left -= 1
