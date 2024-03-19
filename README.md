# Grafos-PCV

## Descrição
O objetivo deste projeto é desenvolver um sistema eficiente para encontrar o caminho mínimo no Problema do Caixeiro Viajante (PCV), ou Traveling Salesman Problem (TSP) em várias instâncias de bases de dados específicas. As bases de dados utilizadas são att48, dantzig42, fri26, gr17 e p01. O TSP é um problema clássico de otimização combinatória em que o objetivo é encontrar o caminho mais curto que visita todos os pontos (cidades) exatamente uma vez e retorna ao ponto de origem.

Bases de Dados:

* att48:     Conjunto de 48 cidades.
* dantzig42: Conjunto de 42 cidades.
* fri26:     Conjunto de 26 cidades.
* gr17:      Conjunto de 17 cidades.
* p01:       Conjunto de 15 cidades.

Todos os algoritmos foram testados utilizando os arquivos de texto(.txt) presentes na pasta "Bases de dados", eles também podem ser encontrados no seguinte site:
https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html

## Instalação
Para todos os três algoritmos vai ser preciso baixar a pasta com o código e os bancos de dados, expecificadamente para o algoritmo de Chritofides vai ser preciso instalar as bibliotecas Numpy e Networkx.
## Como Usar
Você vai precisar executar o codigo seja por terminal, Visual Studio Code, Eclipse etc. e digitar o número do respectivo Banco de Dados.

## Resultados
### Algortimo de Kruskal

* att48:     Custo Minimo : 27670
* dantzig42: Custo Minimo : 591
* fri26:     Custo Minimo : 741
* gr17:      Custo Minimo : 1421
* p01:       Custo Minimo : 260

### Algoritmo de Christofides

* att48:     Custo Minimo : 38475
* dantzig42: Custo Minimo : 773
* fri26:     Custo Minimo : 1051
* gr17:      Custo Minimo : 2197
* p01:       Custo Minimo : 288

### Algoritmo de Dijkstra

* att48:     Custo Minimo : 136489
* dantzig42: Custo Minimo : 3524
* fri26:     Custo Minimo : 3495
* gr17:      Custo Minimo : 4028
* p01:       Custo Minimo : 741

## Licença
MIT License

Copyright (c) [2024] [Uanderson Henrique Batista da Silva, Leonardo Lima e Silva, Saimon Felipe de Lima Santos]


## Contato do desenvolvedor
* Uanderson Henrique Batista da Silva - uanderson_pb@hotmail.com.br - uanderson.silva@arapiraca.ufal.br
* Leonardo Lima e Silva - leo_2002_mario@hotmail.com - leonardo.lima@arapiraca.ufal.br
* Saimon Felipe de Lima Santos - saimonfylps@gmail.com - saimon.santos@arapiraca.ufal.br

## Hardware sugerido
* Intel(R) Core(TM) i3-8100 3.60GHz
* Memória RAM 24 GB (2x4 2666 MHz) (2x8 2666 MHz) DDR4
* HD 1TB
* Sistema operacional Windows 11 64 bits

## Software necessário
Todo o projeto está rodando em Windows 11 versão 23H2 (recomendado).
