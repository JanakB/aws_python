weighted_graph = {
    'A':[('B',3),('D',4)],
    'B':[('C',2),('E',1)],
    'C':[('F',2)],
    'D':[('F',1)],
    'E':[('F',1)],
}
def get_neighbors(v):
    return weighted_graph[v]
 
def h(n):
    H = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E':1,
    'F':1
    }
    
    return H[n]
 
def a_star_algorithm(start, stop):
    visited = set([start])
    unvisited = set([])
    dista = {}
    dista[start] = 0
    adj_map = {}
    adj_map[start] = start
 
    while len(visited) > 0:
        n = None
        for i in visited:
            if n == None or dista[i] + h(i) < dista[n] + h(n):
                n = i;
 
        if n == None:
            print('Path does not exist!')
            return None
 

        if n == stop:
            reconstruction = []
 
            while adj_map[n] != n:
                reconstruction.append(n)
                n = adj_map[n]
 
            reconstruction.append(start)
            reconstruction.reverse()
 
            print('Path found: {}'.format(reconstruction))
            return reconstruction
 

        for (node, weight) in get_neighbors(n):
            if node not in visited and node not in unvisited:
                visited.add(node)
                adj_map[node] = n
                dista[node] = dista[n] + weight
 
            else:
                if dista[node] > dista[n] + weight:
                    dista[node] = dista[n] + weight
                    adj_map[node] = n
 
                    if node in unvisited:
                        unvisited.remove(node)
                        visited.add(node)
 
        visited.remove(n)
        unvisited.add(n)
 
    print('Path does not exist!')
    return None



a_star_algorithm('A', 'F')