# Algoritimo de Ordenação - QUICK SORT

## Módulo Quick Sort com Pybind11 (`quick_sort`)

Este repositório contém a implementação do algoritmo de ordenação **Quick Sort** em C++, com integração para Python utilizando a biblioteca **pybind11**. Além de ordenar os dados, o código coleta métricas de desempenho da execução.

## O Algoritmo: Quick Sort

O **Quick Sort** é um algoritmo de ordenação eficiente que utiliza a estratégia de divisão e conquista. Ele escolhe um elemento como "pivô" e particiona o array ao redor desse pivô, de modo que os elementos menores fiquem à esquerda e os maiores à direita, repetindo o processo recursivamente.

### Como funciona no código (`quick_sort.cpp`):
1. A função principal `quick_sort` recebe um vetor de números de ponto flutuante (`std::vector<float>`) e repassa para a função auxiliar `quick_sort_recursivo`.
2. O `quick_sort_recursivo` define o **pivô** como o elemento central do sub-vetor atual (`vetor[(i + s) / 2]`).
3. Utiliza dois ponteiros (`esq` e `dir`) que percorrem o vetor em direções opostas. O laço `while` compara os elementos com o pivô.
4. Quando encontra elementos no lado errado (maiores à esquerda ou menores à direita do pivô), ocorre uma **troca** (`std::swap`).
5. As métricas são atualizadas a cada comparação, troca e movimentação (como a leitura do pivô ou as trocas).
6. O processo se repete **recursivamente** para as sub-listas à esquerda e à direita do pivô, resultando em uma complexidade de tempo média muito eficiente de **O(n log n)**.

## Métricas Coletadas

Para fins de análise de eficiência, o algoritmo rastreia as seguintes métricas através da estrutura `AlgoritimoMetricas`:
- **Comparações (`comparacoes`):** Quantas vezes os elementos foram comparados com o pivô.
- **Trocas (`trocas`):** Quantas vezes os elementos mudaram de posição.
- **Movimentações (`movimentacoes`):** Quantas operações de memória ocorreram (incluindo a leitura inicial do pivô e as trocas, onde cada troca conta como 3 movimentações).
- **Tempo (`tempo`):** O tempo total de execução da ordenação, convertido para milissegundos usando `clock()`.

As métricas da última execução são armazenadas na estrutura global `metricas.quick`. Você pode recuperá-las chamando a função `get_metricas()`.

## 🐍 Integração com o Sistema via `pybind11`

O arquivo `quick_sort.cpp` atua como uma ponte (wrapper) para que funções escritas em C++ de alta performance possam ser chamadas nativamente a partir de um script Python.

### Como o `pybind11` faz isso:
1. **Conversão Automática de Tipos (STL):** Graças ao include `<pybind11/stl.h>`, o `pybind11` sabe como converter automaticamente o `std::vector<float>` do C++ para uma lista nativa do Python (e vice-versa).
2. **Definição do Módulo:** A macro `PYBIND11_MODULE(quick_sort, m)` inicializa o módulo e o batiza como `quick_sort`. Este será o nome usado no `import` do Python.
3. **Exposição das Funções e Classes (`m.def` e `pybind11::class_`):** 
   - `m.def("quick_sort", &quick_sort)`: Diz ao Python que a função C++ `quick_sort` existirá no módulo sob o mesmo nome.
   - `pybind11::class_<AlgoritimoMetricas>(m, "AlgoritimoMetricas")`: Registra a estrutura customizada de métricas e expõe seus atributos como leitura (`def_readonly`), permitindo que o Python entenda o tipo retornado pelo C++.
   - `m.def("get_metricas", &get_metricas)`: Expõe a função de coleta de métricas para ser chamada pelo Python.