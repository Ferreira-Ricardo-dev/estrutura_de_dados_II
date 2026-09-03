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

std::vector<AlgoritimoMetricas> get_metricas() {
    std::vector<AlgoritimoMetricas> metricas_vetor;
    metricas_vetor.push_back(metricas.bubble);
    return metricas_vetor;
}
PYBIND11_MODULE(blubble_sort, m) {
    m.def("bubble_sort", &bubble_sort);
    pybind11::class_<AlgoritimoMetricas>(m, "AlgoritimoMetricas")
        .def_readonly("comparacoes", &AlgoritimoMetricas::comparacoes)
        .def_readonly("trocas", &AlgoritimoMetricas::trocas)
        .def_readonly("movimentacoes", & AlgoritimoMetricas::movimentacoes)
        .def_readonly("tempo", &AlgoritimoMetricas::tempo);
    m.def("get_metricas", &get_metricas);
}