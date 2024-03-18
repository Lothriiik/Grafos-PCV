class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    # Adiciona uma aresta ao grafo
    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    # Função para encontrar conjunto de um elemento "i"
    def find(self, pai, i):
        if pai[i] == i:
            return i
        return self.find(pai, pai[i])

    # Função que une dois conjuntos de x e y
    def union(self, pai, rank, x, y):
        raiz_x = self.find(pai, x)
        raiz_y = self.find(pai, y)

        # Anexa menor árvore sob maior raiz
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x

        # Se as alturas são as mesmas, então faça uma delas
        # como raiz e incremente a altura da árvore (rank)
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    # O algoritmo de Kruskal
    def kruskal(self):
        resultado = []  # Esta será a árvore geradora mínima
        i, e = 0, 0  # Índice usado para o resultado[] e arestas selecionadas

        # Passo 1: Ordenar todas as arestas em ordem não decrescente de acordo com seus pesos
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        pai = []
        rank = []

        # Cria V subconjuntos com elementos únicos
        for node in range(self.V):
            pai.append(node)
            rank.append(0)

        # Número de arestas a serem tomadas é igual a V-1
        while e < self.V - 1:
            # Passo 2: Escolha a menor aresta e incrementa o índice para a próxima iteração
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.find(pai, u)
            y = self.find(pai, v)

            # Se incluir essa aresta não forma um ciclo, inclue ela no resultado e incrementa o índice de resultado
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(pai, rank, x, y)
            # Senão, descarte a aresta

        return resultado

# Função que lê o arquivo e retornar uma matriz de adjacência
def ler_arquivo(caminho_arquivo):
    matriz_adjacente = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().split()
            linha = [int(elemento) for elemento in linha]
            matriz_adjacente.append(linha)
    return matriz_adjacente

# Função para calcular o custo total do tour
def calcular_custo_total(arvore):
    custo_total = sum(aresta[2] for aresta in arvore)
    return custo_total

# Função para criar a matriz de adjacência correspondente à AGM
def matriz_adjacente_agm(arvore, vertices):
    matriz_adjacente = [[int('0')] * vertices for _ in range(vertices)]
    for u, v, w in arvore:
        matriz_adjacente[u][v] = w
        matriz_adjacente[v][u] = w
    return matriz_adjacente

# Função principal
def main(caminho_arquivo):
    matriz_adjacente = ler_arquivo(caminho_arquivo)
    num_vertices = len(matriz_adjacente)
    grafo = Grafo(num_vertices)

    # Construindo o grafo com base na matriz de adjacência lida
    for i in range(num_vertices):
        for j in range(num_vertices):
            if matriz_adjacente[i][j] != 0:
                grafo.add_aresta(i, j, matriz_adjacente[i][j])

    # Encontrando a AGM usando o algoritmo de Kruskal
    arvore_geradora_minima = grafo.kruskal()

    # Calculando o custo total da AGM
    custo_total = calcular_custo_total(arvore_geradora_minima)

    # Criando a matriz de adjacência da AGM
    matriz_adjacente_agm_ = matriz_adjacente_agm(arvore_geradora_minima, num_vertices)

    return arvore_geradora_minima, matriz_adjacente_agm_, custo_total

# Escolha do arquivo .txt a ser lido e execução geral
caminho_arquivo = input("Digite o caminho completo do arquivo .txt: ")
arvore_minima, matriz_adjacente_agm, custo_total = main(caminho_arquivo)

#Escrevem no terminal a AGM, a matriz e o custo total
print("Árvore Geradora Mínima:")
for aresta in arvore_minima:
    print(aresta)

print("\nMatriz de Adjacência da AGM:")
for linha in matriz_adjacente_agm:
    print(linha)
    
print("\nCusto Total do tour da AGM:", custo_total)
