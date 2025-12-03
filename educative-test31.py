from collections import defaultdict

def build_node_dist_matrix(adj_map, dist_grid, st_idx, node_idx, dist ):
    dist_grid[st_idx][node_idx] = dist
    for adj_node in adj_map[node_idx]:
        if dist_grid[st_idx][adj_node] == -1:
            build_node_dist_matrix(adj_map, dist_grid, st_idx, adj_node, dist+1 )

def find_closest_path_node(adj_map, dist_grid, st_idx, end_idx, target_idx, ans_idx):
    for neigh in adj_map[st_idx]:
        # compare distance to end node in comparision with the start node
        # Tree has only unique path between two nodes that passes only through 1 neighbour only
        if dist_grid[end_idx][st_idx] > dist_grid[end_idx][neigh]:
            # Compute the answer node comparision with the new start node
            if dist_grid[target_idx][ans_idx] > dist_grid[target_idx][neigh]:
                ans_idx = neigh
            ans_idx = find_closest_path_node(adj_map, dist_grid, neigh, end_idx, target_idx, ans_idx)
    return ans_idx

def closestNode(n, edges, query):    
    ans_nodes = []
    dist_grid = [[-1]*n for _ in range(n)]
    adj_map = defaultdict(list)
    for u,v in edges:
        adj_map[u].append(v)
        adj_map[v].append(u)
    for idx in range(n):
        adj_map[idx].sort()
        build_node_dist_matrix(adj_map, dist_grid, idx,idx,0)
    
    # process the Query with the adjacency list and distane matrix.
    idx = 0
    ans_nodes = [-1] * len(query)
    for st_idx, end_idx, target_idx in query:
        ans_nodes[idx] = find_closest_path_node(adj_map, dist_grid, st_idx, end_idx, target_idx, st_idx)
        idx += 1
    return ans_nodes

print(closestNode(7,[[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]],[[5,3,4],[5,3,6]]))