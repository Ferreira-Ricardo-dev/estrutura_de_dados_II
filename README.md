# Atividade Avaliativa – Estruturas de Dados: Arrays, Matrizes, Algoritmos de Ordenação e Busca

Bem-vindo ao repositório do nosso trabalho prático da disciplina de Estruturas de Dados II! Este projeto tem como objetivo investigar experimentalmente o comportamento de estruturas de dados e algoritmos fundamentais. Através de implementações em C++ e integração com Python, analisamos a relação entre arrays, matrizes, algoritmos de ordenação, busca, índices, loops e complexidade computacional.

O diferencial deste projeto não é apenas ordenar ou buscar dados, mas **medir, comparar e interpretar** o custo dessas operações e a eficiência de cada abordagem.

## 👥 Autores
* Guilherme 
* Gustavo 
* Lucas
* Pedro
* Ricardo 


## 🛠️ Pré-requisitos
Para rodar este projeto, você precisará de:
* Um compilador C++ (como o `clang` no macOS ou `gcc` no Linux/Windows).
* Python 3 instalado.
* Biblioteca `pybind11` instalada no ambiente Python.

## 🚀 Como compilar e executar

1. Crie e ative um ambiente virtual para não conflitar com as dependências do seu sistema:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Navegue até o diretório `setup` (ou onde o seu `setup.py` estiver localizado) e insira no terminal o comando para compilar os módulos C++:
   ```bash
   python setup.py build_ext --inplace
   ```

## 🧩 O que você encontrará neste projeto?

Este projeto foi estruturado para cumprir os requisitos da atividade avaliativa e inclui módulos automatizados, como um "robô" interno responsável por gerar os arrays e matrizes de teste aleatoriamente, garantindo testes justos e escaláveis.

O desenvolvimento foi dividido nas seguintes frentes:

* **Comparação de Ordenação (Bubble Sort vs. Quick Sort):** Implementação e coleta de métricas (comparações, trocas, movimentações e tempo) de ambos os algoritmos aplicados exatamente aos mesmos conjuntos de dados de 10, 20 e 1.000 elementos.
* **Investigação de Busca em Matrizes:** Implementação de busca sequencial com loops aninhados em matrizes de tamanhos variados (2x2, 10x10 e 100x100), rastreando a quantidade de comparações no melhor caso, pior caso e caso médio.
* **Hands On 1 - Arrays:** Sistema de manipulação de um array de temperaturas, explorando média, maior valor, menor valor e contagem de métricas, com análise das operações de percurso.
* **Hands On 2 - Matrizes Aplicadas (Monitoramento de Sensores):** Um sistema mais complexo simulando sensores em uma matriz (linhas como sensores e colunas como horários). Explora cálculos globais, buscas específicas (maior leitura e qual sensor/horário) e filtragem de dados através de varredura bidimensional.

O grande objetivo de todas essas implementações é provar na prática que: *dois algoritmos podem produzir exatamente o mesmo resultado e, ainda assim, realizar quantidades completamente diferentes de operações dependendo do tamanho da entrada.*

## Por que analisar apenas o resultado?

Porque diferentes algoritmos podem chegar ao mesmo resultado, mas gastar tempos e quantidades de operações diferentes.

Por isso, é importante analisar:

- Tempo de execução
- Número de operações
- Complexidade
- Uso de memória
