import itertools

import numpy as np
import networkx as nx

from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

from utils import minimal_spanning_tree


def christofides_tsp(graph, starting_node=0):
    
    mst = minimal_spanning_tree(graph, 'Prim', starting_node=0)
    odd_degree_nodes = list(_get_odd_degree_vertices(mst))
    odd_degree_nodes_ix = np.ix_(odd_degree_nodes, odd_degree_nodes)
    nx_graph = nx.from_numpy_array(-1 * graph[odd_degree_nodes_ix])
    matching = max_weight_matching(nx_graph, maxcardinality=True)
    euler_multigraph = nx.MultiGraph(mst)
    for edge in matching:
        euler_multigraph.add_edge(odd_degree_nodes[edge[0]], odd_degree_nodes[edge[1]],
                                  weight=graph[odd_degree_nodes[edge[0]]][odd_degree_nodes[edge[1]]])
    euler_tour = list(eulerian_circuit(euler_multigraph, source=starting_node))
    path = list(itertools.chain.from_iterable(euler_tour))
    return _remove_repeated_vertices(path, starting_node)[:-1]


def _get_odd_degree_vertices(graph):

    odd_degree_vertices = set()
    for index, row in enumerate(graph):
        if len(np.nonzero(row)[0]) % 2 != 0:
            odd_degree_vertices.add(index)
    return odd_degree_vertices


def _remove_repeated_vertices(path, starting_node):
    path = list(dict.fromkeys(path).keys())
    path.append(starting_node)
    return path

def tour_cost(adj_matrix, tour):
    cost = 0
    for i in range(len(tour)):
        u = tour[i]
        v = tour[(i + 1) % len(tour)]
        cost += adj_matrix[u][v]
    return cost

def escolhaBanco():
    # Realiza a escolha do respectivo Banco de Dados
    print('Escolha o Banco de dados:')
    print('1 - att48')
    print('2 - dantzig42')
    print('3 - fri26')
    print('4 - gr17')
    print('5 - p01')
    print()
    escolha = str(input('Digite o número do respectivo Banco de dados: '))

    if escolha == '1':
        bancodeDados = "att48_d.txt"
        return bancodeDados
    if escolha == '2':
        bancodeDados = "dantzig42_d.txt"
        return bancodeDados
    if escolha == '3':
        bancodeDados = "fri26_d.txt"
        return bancodeDados
    if escolha == '4':
        bancodeDados = "gr17_d.txt"
        return bancodeDados
    if escolha == '5':
        bancodeDados = "p01_d.txt"
        return bancodeDados
    else:
        print('')
        print('Não existe essa opção.')
        print('')
        return escolhaBanco()


def lerArquivoTsp(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Inicializa a variável dados
    dados = []
    indiceSecao=0

    # Processar as linhas de pesos de arestas ou coordenadas
    numCidades = len(linhas) - indiceSecao

    # Inicializa a variável matrixDistancias
    matrixDistancias = []

    for i in range(indiceSecao, indiceSecao + numCidades):
        linhaStriped = linhas[i].strip()
        distancias = list(map(float, linhaStriped.split()))
        matrixDistancias.append(distancias)


    dados = matrixDistancias



    return dados


def main():
    # Caminho do arquivo .tsp (substitua pelo caminho do seu arquivo)
    bancodeDados = escolhaBanco()

    caminhoArquivo = bancodeDados

    # Chama a função para ler os dados (pesos de arestas)
    dados = lerArquivoTsp(caminhoArquivo)

    # Exibe os dados

    graph = np.array(dados)
    print(graph)
    print(christofides_tsp(graph))
    print("Custo mínimo do tour:", tour_cost(graph, christofides_tsp(graph)))

if __name__ == "__main__":
    main()