# Algoritimo de Ordenação - BUBBLE SORT

## Módulo Bubble Sort com Pybind11 (`blubble_sort`)

Este repositório contém a implementação do algoritmo de ordenação **Bubble Sort** em C++, com integração para Python utilizando a biblioteca **pybind11**. Além de ordenar os dados, o código coleta métricas de desempenho da execução.

## O Algoritmo: Bubble Sort

O **Bubble Sort** (Ordenação por Flutuação) é um algoritmo de ordenação simples. Ele iterando repetidamente pela lista, comparando elementos adjacentes e trocando-os de lugar se estiverem na ordem errada.

### Como funciona no código (`blubble_sort.cpp`):
1. A função `bubble_sort` recebe um vetor de números de ponto flutuante (`std::vector<float>`).
2. Utiliza dois laços de repetição (`for` aninhados):
   - O laço externo controla as passagens pela lista (vai até `qtd - 1`).
   - O laço interno realiza as comparações entre os elementos adjacentes (`vetor[j] > vetor[j + 1]`).
3. Se o elemento atual for maior que o próximo, ocorre uma **troca** (`std::swap`).
4. Cada vez que isso acontece, as métricas de desempenho são atualizadas.
5. O processo se repete até que o vetor esteja completamente ordenado, resultando em uma complexidade de tempo de **O(n²)** no pior caso.

## Métricas Coletadas

Para fins de análise de eficiência, o algoritmo rastreia as seguintes métricas através da estrutura `AlgoritimoMetricas`:
- **Comparações (`comparacoes`):** Quantas vezes dois elementos foram comparados dentro do `if`.
- **Trocas (`trocas`):** Quantas vezes os elementos mudaram de posição.
- **Movimentações (`movimentacoes`):** Quantas operações de memória ocorreram (neste código, cada troca conta como 3 movimentações: leitura, armazenamento temporário e reescrita).
- **Tempo (`tempo`):** O tempo total de execução do loop principal, convertido para milissegundos usando `clock()`.

As métricas da última execução são armazenadas na variável global `metricas.bubble`. Você pode recuperá-las chamando a função `get_metricas()`.

## 🐍 Integração com o Sistema via `pybind11`

O arquivo `blubble_sort.cpp` atua como uma ponte (wrapper) para que funções escritas em C++ de alta performance possam ser chamadas nativamente a partir de um script Python.

### Como o `pybind11` faz isso:
1. **Conversão Automática de Tipos (STL):** Graças ao include `<pybind11/stl.h>`, o `pybind11` sabe como converter automaticamente o `std::vector<float>` do C++ para uma lista nativa do Python (e vice-versa) durante a chamada da função.
2. **Definição do Módulo:** A macro `PYBIND11_MODULE(blubble_sort, m)` inicializa o módulo e o batiza como `blubble_sort`. Este será o nome usado no `import` do Python.
3. **Exposição das Funções (`m.def`):** 
   - `m.def("bubble_sort", &bubble_sort)`: Diz ao Python que a função C++ `bubble_sort` existirá no módulo sob o mesmo nome.
   - `m.def("get_metricas", &get_metricas)`: Expõe a função de coleta de métricas.

