inf = float('inf')
G = [[0,4,inf,inf,3,inf,inf,inf],
     [4,0,5,inf,2,inf,inf,inf],
     [inf,5,0,5,3,1,inf,inf],
     [inf,inf,5,0,inf,inf,2,7],
     [3,2,3,inf,0,6,inf,inf],
     [inf,inf,1,inf,6,0,5,inf],
     [inf,inf,inf,2,inf,5,0,4],
     [inf,inf,inf,7,inf,inf,4,0]]
vertices_names = ['a','b','c','d','e','f','g', 'z']
vertices_names_nums = {vertices_names[i]: i for i in range(len(vertices_names))}

def dijkstra_algorithm(G, vertices_names_nums):
    inf = float('inf')
    unvisited_vertices = {i:inf for i in range(len(vertices_names_nums))}
    visited_vertices = {}
    current_path_len = 0
    current_vertex = 0
    visited_vertices[current_vertex] = current_path_len
    del unvisited_vertices[current_vertex]

    while len(unvisited_vertices) > 0:
        for elem in unvisited_vertices.keys():
            if G[current_vertex][elem] == inf:
                continue
            elif current_path_len + G[current_vertex][elem] < unvisited_vertices[elem]:
                unvisited_vertices[elem] = current_path_len + G[current_vertex][elem]

        current_path_len = minimum(list(unvisited_vertices.values()))
        current_vertex = find_key_by_value(unvisited_vertices, current_path_len)
        visited_vertices[current_vertex] = current_path_len
        del unvisited_vertices[current_vertex]
    return compose(vertices_names_nums, visited_vertices)

def minimum(list):
    m = list[0]
    for elem in list:
        if elem < m:
            m = elem
    return m

def find_key_by_value(dict, value):
    for actual_key, actual_value in dict.items():
        if actual_value == value:
            return actual_key

def compose(dict_1, dict_2):
    composition = {key:dict_2[value] for key, value in dict_1.items()}
    return composition


print (dijkstra_algorithm(G,vertices_names_nums))

