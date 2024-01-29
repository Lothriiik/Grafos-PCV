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
        bancodeDados = "att48.tsp"
        return bancodeDados
    if escolha == '2':
        bancodeDados = "dantzig42.tsp"
        return bancodeDados
    if escolha == '3':
        bancodeDados = "fri26.tsp"
        return bancodeDados
    if escolha == '4':
        bancodeDados = "gr17.tsp"
        return bancodeDados
    if escolha == '5':
        bancodeDados = "p01.tsp"
        return bancodeDados
    else:
        print('')
        print('Não existe essa opção.')
        print('')
        return escolhaBanco()


def lerArquivoTsp(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Verifica automaticamente o formato do arquivo TSP
    formatoArquivo = None
    for linha in linhas:
        if "EDGE_WEIGHT_SECTION" in linha:
            formatoArquivo = "EDGE_WEIGHT_SECTION"
            break
        elif "NODE_COORD_SECTION" in linha:
            formatoArquivo = "NODE_COORD_SECTION"
            break

    # Inicializa a variável dados
    dados = []

    # Processa as linhas conforme o formato identificado
    if formatoArquivo == "NODE_COORD_SECTION":
        indiceSecao = linhas.index("NODE_COORD_SECTION\n") + 1
        dados = [linha.strip().split()[1:] for linha in linhas[indiceSecao:-1]]
        dados = [(float(x), float(y)) for x, y in dados]
    elif formatoArquivo == "EDGE_WEIGHT_SECTION":
        indiceSecao = linhas.index("EDGE_WEIGHT_SECTION\n") + 1

        # Verificar se há DISPLAY_DATA_SECTION
        if "DISPLAY_DATA_SECTION" in linhas:
            indiceSecaoDisplay = linhas.index("DISPLAY_DATA_SECTION\n") + 1
            linhas = linhas[indiceSecaoDisplay:]

        # Processar as linhas de pesos de arestas ou coordenadas
        numCidades = len(linhas) - indiceSecao

        # Inicializa a variável matrixDistancias
        matrixDistancias = []

        # Limita as linhas pra que parem em 'EOF' 'DISPLAY_DATA_SECTION' 'TOUR_SECTION' que e quando termina a matriz
        for i in range(indiceSecao, indiceSecao + numCidades):
            linhaStriped = linhas[i].strip()

            if linhaStriped == 'EOF':
                break
            if linhaStriped == 'DISPLAY_DATA_SECTION':
                break
            if linhaStriped == 'TOUR_SECTION':
                break

            # Adicionar cada valor da linha como float
            distancias = list(map(float, linhaStriped.split()))
            matrixDistancias.append(distancias)

        dados = matrixDistancias

    elif formatoArquivo == "DISPLAY_DATA_SECTION" and "EDGE_WEIGHT_SECTION" in linhas:
        indiceSecao = linhas.index("EDGE_WEIGHT_SECTION\n") + 1
        numCidades = len(linhas) - indiceSecao

        # Inicializa a variável matrix_distancias
        matrixDistancias = []

        for i in range(indiceSecao, indiceSecao + numCidades):
            linhaStriped = linhas[i].strip()

            if linhaStriped == 'EOF':
                break

            # Adicionar cada valor da linha como float
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
    print("Dados:")
    print(dados)

if __name__ == "__main__":
    main()
