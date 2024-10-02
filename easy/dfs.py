'''Дан неориентированный граф, 
возможно с петлями и кратными ребрами. 
Необходимо найти компоненту связности, 
содержащую вершину с номером 1.'''


def dfs(graph: list[list], current_vertex: int, visited: list, res_list: list):
    visited[current_vertex] = 1
    res_list.append(current_vertex + 1)

    for neighbor_vertex in graph[current_vertex]:
        if visited[neighbor_vertex] != 1:
            dfs(graph, neighbor_vertex, visited, res_list)


n, m = list(map(int, input().split()))

list_of_adequacy = [[] * n for i in range(n)]
list_of_visited = [0 for i in range(n)]

# Вывод списков соседей вершин 
for i in range(len(list_of_adequacy)):
    print(str(i) + ":", list_of_adequacy[i])
    
for i in range(m):
    vertex_1, vertex_2 = list(map(int, input().split()))
    list_of_adequacy[vertex_1 - 1].append(vertex_2 - 1)
    list_of_adequacy[vertex_2 - 1].append(vertex_1 - 1)

vertex_list = []

# необходимо найти компоненту связности где есть вершина с номером 1
# поэтому начинаем поиск с "первой" вершины т.е. вершины с номером в списке - 0
dfs(graph=list_of_adequacy, current_vertex=0, visited=list_of_visited, res_list=vertex_list)

vertex_list.sort()

print(len(vertex_list))
for i in range(len(vertex_list)):
    print(vertex_list[i], end=" ")