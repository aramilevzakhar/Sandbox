import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

colors = ['Red', 'Blue', 'Green', 'Yellow',  'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,5),(1,3),(1,2),(1,4),(4,5)])
# G.add_nodes_from([1,2,3,4])
# G.add_edges_from([(1,2),(2,3),(3,4),(1,4)])
colors_of_nodes={}
# перебираем всех соседов и смотрим какие у них цвета 
def coloring(node, color):
    # G.neighbors(node) - это список всех соседей
    # neighbor - это один сосед
    for neighbor in G.neighbors(node):
        # neighbor contains all sosedi node
        # если colors_of_nodes содержит 
        #смотрим в список имеющихся цветов
        color_of_neighbor = colors_of_nodes.get(neighbor, None)
        #print('neighbor:', neighbor, 'color_of_neighbor: ', color_of_neighbor, 'colors_of_nodes.get(neighbor, None): ', colors_of_nodes.get(neighbor, None))
        # на 1-ой итерации так как список пуст эта функция вернёт True
        # если у перебираемого соседа такой же цвет как и в выбранном то отклоняем и выбираем следующий цвет(переходим в функцию get_color_for_node)
        if color_of_neighbor == color:
            return False
    # в это случае мы добавляем новый свет к node иначе просто сменяем его
    return True
def get_color_for_node(node):
    for color in colors:
        if coloring(node, color):
            return color
def main():
    # while all nodes
    for node in G.nodes():
        print(node) 
        colors_of_nodes[node] = get_color_for_node(node)
    print(colors_of_nodes)
main()
l = set()
for el in colors_of_nodes:
    print(colors_of_nodes[el])
    l.add(colors_of_nodes[el])
print('Chromatic_number_search: ', len(l))
# print(G.nodes())
# print(G.edges())
# print(list(G.neighbors(1)))
# print(list(G.neighbors(2)))
# print(list(G.neighbors(3)))
# print(list(G.neighbors(4)))
# print(list(G.neighbors(5)))
# for el in G.neighbors(3):
#     print(el)
# 
# G.add_node('123')
# print(G.nodes())













