#include <vector>
#include <stdlib.h>
#include <time.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

struct AlgoritimoMetricas {
    int comparacoes;
    int trocas;
    int movimentacoes;
    double tempo;
};
struct {
    AlgoritimoMetricas bubble;
} metricas;

std::vector<float> bubble_sort (std::vector<float> vetor) {
    metricas.bubble.trocas = 0;
    metricas.bubble.comparacoes = 0;
    metricas.bubble.movimentacoes = 0;

    int qtd = vetor.size();

    clock_t start = clock();
     for (int i = 0; i< qtd - 1; i++) { 
        for (int j = 0; j < qtd - 1 - i; j++) { 
            metricas.bubble.comparacoes++;
            if (vetor[j] > vetor[j + 1]) { 
                std::swap(vetor[j], vetor[j + 1]);
                metricas.bubble.trocas++;
                metricas.bubble.movimentacoes += 3;
            }
        }
    }
    clock_t end = clock();
    metricas.bubble.tempo = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    return vetor;
}

PYBIND11_MODULE(blubble_sort, m) {
    m.def("bubble_sort", &bubble_sort, "Ordena um vetor usando o algoritmo Bubble Sort");
}