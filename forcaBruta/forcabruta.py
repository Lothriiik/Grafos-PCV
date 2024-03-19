import timeit
import numpy as np
from sys import maxsize
from itertools import permutations

def calcular_custo(caminho, matriz):    # calcula o custo do caminho
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i+1]]
    custo += matriz[caminho[-1]][caminho[0]]  
    return custo

def forca_bruta(grafo, inicio):
    # Salvando os vértices
    vertices = []
    for vert in range(len(grafo)):
        if vert != inicio:
            vertices.append(vert)

    prox = permutations(vertices)
    caminhoAtual = maxsize

    # Fazendo o cálculo de custo
    for vert in prox:
        custoAtual = 0
        x = inicio

        for aresta in vert:
            custoAtual += float(grafo[x][aresta])
            x = aresta
        custoAtual += float(grafo[x][inicio])
        caminhoMin = min(caminhoAtual, custoAtual)

        if caminhoMin < caminhoAtual:
            caminhoAtual = min(caminhoAtual, custoAtual)
            aux = vert

    # Decidindo o melhor caminho
    melhorCaminho = []
    for vert in aux:
        melhorCaminho.append(vert)

    melhorCaminho.insert(0, inicio)
    melhorCaminho.append(inicio)

    return caminhoAtual, melhorCaminho

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
    print(testar(graph))


def testar(matriz):   #aplica as funções nas matrizes
    inicio_total = timeit.default_timer()  
    custo_total_forca_bruta, _ = forca_bruta(matriz, 0)    
    fim_total = timeit.default_timer()  
    tempo_total = (fim_total - inicio_total)   
        

    print(f"Tempo Total: {tempo_total:.3f} s")
    print(f"Custo Total Força Bruta: {custo_total_forca_bruta}")

if __name__ == "__main__":
    main()