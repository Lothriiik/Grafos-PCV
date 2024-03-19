#import numpy as np
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
        bancodeDados = "C:/Users/saimo/OneDrive/Documentos/JAVA_PROJECTS/ACE6/att48_d.txt"
        return bancodeDados
    if escolha == '2':
        bancodeDados = "C:/Users/saimo/OneDrive/Documentos/JAVA_PROJECTS/ACE6/dantzig42_d.txt"
        return bancodeDados
    if escolha == '3':
        bancodeDados = "C:/Users/saimo/OneDrive/Documentos/JAVA_PROJECTS/ACE6/fri26_d.txt"
        return bancodeDados
    if escolha == '4':
        bancodeDados = "C:/Users/saimo/OneDrive/Documentos/JAVA_PROJECTS/ACE6/gr17_d.txt"
        return bancodeDados
    if escolha == '5':
        bancodeDados = "C:/Users/saimo/OneDrive/Documentos/JAVA_PROJECTS/ACE6/p01_d.txt"
        return bancodeDados
    else:
        print('')
        print('Não existe essa opção.')
        print('')
        return escolhaBanco()



import sys

def dijkstra(matriz_adjacencia, origem):
    num_vertices = len(matriz_adjacencia)
    distancia = [sys.maxsize] * num_vertices  # Inicializa todas as distâncias como infinito
    distancia[origem] = 0  # A distância da origem para ela mesma é 0
    visitados = [False] * num_vertices  # Mantém o controle de quais vértices foram visitados

    for _ in range(num_vertices):
        # Encontra o vértice com a menor distância entre os não visitados
        menor_distancia = sys.maxsize
        for i in range(num_vertices):
            if distancia[i] < menor_distancia and not visitados[i]:
                menor_distancia = distancia[i]
                vertice_atual = i

        # Marca o vértice atual como visitado
        visitados[vertice_atual] = True

        # Atualiza a distância dos vértices adjacentes ao vértice atual
        for vizinho in range(num_vertices):
            if (not visitados[vizinho] and
                    matriz_adjacencia[vertice_atual][vizinho] != 0 and
                    distancia[vertice_atual] + matriz_adjacencia[vertice_atual][vizinho] < distancia[vizinho]):
                distancia[vizinho] = distancia[vertice_atual] + matriz_adjacencia[vertice_atual][vizinho]

    return distancia


def calcular_custo_minimo(matriz_adjacencia, origem):
    distancia = dijkstra(matriz_adjacencia, origem)
    total_cost = sum(distancia) # Somando todas as distâncias encontradas
    return total_cost


def main():
    # Caminho do arquivo .tsp (substitua pelo caminho do seu arquivo)
    bancodeDados = escolhaBanco()

    caminhoArquivo = bancodeDados

    # Chama a função para ler os dados (pesos de arestas)
    dados = ler_arquivo_txt(caminhoArquivo)

    # Exibe os dados
    origem = 0
    resultados_dijkstra = dijkstra(dados, origem)
    print("Distâncias mínimas a partir do vértice de origem", origem)
    for vertice, distancia in enumerate(resultados_dijkstra):
        print(f"Vértice {vertice}: Distância = {distancia}")
    print("O custo minimo é: ", calcular_custo_minimo(dados, origem))

def ler_arquivo_txt(nome_arquivo):
    matriz = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()  # Remove espaços em branco no início e no final da linha
            elementos = linha.split()  # Divide a linha em elementos usando espaços em branco como separador
            elementos_sem_espacos = [elemento.replace(' ', '') for elemento in elementos]  # Remove espaços entre os números
            elementos_inteiros = [int(elemento) for elemento in elementos_sem_espacos]  # Converte os elementos para inteiros
            matriz.append(elementos_inteiros)  # Adiciona a linha à matriz
    return matriz

main()