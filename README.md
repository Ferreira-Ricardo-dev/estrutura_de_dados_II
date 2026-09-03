# Comparação de Algoritmos de Ordenação (C++ e Python)

Este repositório contém a Atividade Avaliativa I da disciplina de Estrutura de Dados II (Engenharia de Software, 3º Semestre - UDF). 

O projeto implementa e compara o desempenho dos algoritmos **Bubble Sort** e **Quick Sort**. Para unir alta performance e facilidade de uso, a lógica matemática e a geração de sequências aleatórias foram desenvolvidas em C++ puro e exportadas como módulos dinâmicos para Python utilizando a biblioteca `pybind11`.

**Autores**
* Guilherme 
* Ricardo 
* Gustavo 

**Pré-requisitos**
Para rodar este projeto, você precisará de um compilador C++ (como o `clang` no macOS), Python 3 instalado e a biblioteca `pybind11`.

**Como compilar e executar**

1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate


# Análise de Algoritmos

## O tamanho dos dados influencia as operações?

Sim. Quanto maior a quantidade de elementos, maior pode ser o número de operações.

## Bubble Sort x Quick Sort

- **Bubble Sort:** O(n²), fica mais lento com muitos elementos.
- **Quick Sort:** O(n log n) em média, sendo geralmente mais rápido.

## Por que analisar apenas o resultado?

Porque dois algoritmos podem chegar ao mesmo resultado, mas gastar tempos e quantidades de operações diferentes.

Por isso, é importante analisar:

- Tempo de execução
- Número de operações
- Complexidade
- Uso de memória
