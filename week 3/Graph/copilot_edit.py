'''Graph'''

def get_graph_from_file(file_name:str) -> list:
    """ 
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding= 'utf-8') as f:
        text = f.readlines()
        result = []
        for x in text:
            if '\n' in x:
                x =  x.replace('\n', '')
            result.append([int(a) for a in x.split(',')])
        return result

def to_edge_dict(edge_list:list) -> dict:
    """ 
    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    result = {}
    numbers = []
    for x in edge_list:
        numbers.extend(x)
    numbers = set(numbers)
    for num in numbers:
        a = []
        for li in edge_list:
            if num in li:
                if li.index(num) == 0:
                    b = li[1]
                else:
                    b = li[0]
                if b not in a:
                    a.append(b)
        result[num] = sorted(a)
        a = []
    return result

def is_edge_in_graph(graph:dict, edge:tuple) -> bool:
    """ 
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return bool(edge[0] in graph.keys() and edge[1] in graph[edge[0]])

def add_edge(graph:dict, edge:tuple) -> dict:
    """ 
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if is_edge_in_graph(graph, edge) is False:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def del_edge(graph:dict, edge:tuple) -> dict:
    """ 
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if is_edge_in_graph(graph, edge):
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
    return graph

def add_node(graph:dict, node:int) -> dict:
    """ 
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph

def del_node(graph:dict, node:int) -> dict:
    """ 
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        del graph[node]
        for val in graph.values():
            if node in val:
                val.remove(node)
    return graph
def convert_to_dot(filename:str) -> None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete = False, encoding = 'utf-8') as tmpfile:
    ...     _= tmpfile.write('1,2\\n3,4\\n1,5')
    >>> convert_to_dot(tmpfile.name)
    >>> with open(tmpfile.name, mode = 'r', encoding='utf-8') as f:
    ...     _= result = f.read()
    >>> print(result)
    digraph {
    1 -> 2
    1 -> 5
    2 -> 1
    3 -> 4
    4 -> 3
    5 -> 1
    }
    """
    a = get_graph_from_file(filename)
    graph = to_edge_dict(a)
    new_name = filename.replace('.txt','.dot')
    with open(new_name, 'w', encoding='utf-8') as f:
        dot_graph = 'digraph {\n'
        for key, val in graph.items():
            for x in val:
                dot_graph += f'{key} -> {x}\n'
        dot_graph += '}'
        f.write(dot_graph)