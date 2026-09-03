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
    AlgoritimoMetricas quick;
} metricas;


void quick_sort_recursivo(std::vector<float>& vetor, int i, int s) {
    int esq = i, dir = s;
    float pivo = vetor[(i + s) / 2];
    metricas.quick.movimentacoes++;
    
    while (esq <= dir) {
        metricas.quick.comparacoes++;
        while (vetor[esq] < pivo) {
            esq++;
            metricas.quick.comparacoes++;
        }
        while (vetor[dir] > pivo) {
            dir--;
            metricas.quick.comparacoes++;
        }
        if (esq <= dir) {
            if (esq != dir) {
                std::swap(vetor[esq], vetor[dir]);
                metricas.quick.trocas++;
                metricas.quick.movimentacoes += 3;
            }
            esq++;
            dir--;
        }
    }

    if (i < dir) {
        quick_sort_recursivo(vetor, i, dir);
    }
    if (esq < s) {
        quick_sort_recursivo(vetor, esq, s);
    }
    
} 

std::vector<float> quick_sort(std::vector<float> vetor) {
    metricas.quick.trocas = 0;
    metricas.quick.comparacoes = 0;
    metricas.quick.movimentacoes = 0;

    int qtd = vetor.size();

    clock_t start = clock();
    if (!vetor.empty()) quick_sort_recursivo(vetor, 0, qtd - 1);
    
    clock_t end = clock();
    metricas.quick.tempo = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    return vetor;
}

PYBIND11_MODULE(quick_sort, m) {
    m.def("quick_sort", &quick_sort);
}