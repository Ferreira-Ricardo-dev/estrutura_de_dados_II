#include <vector>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


std::vector<float> criar_sequencia  (int qtd, int tam_max_exp) {
    std::vector<float> vetor;
    vetor.reserve(qtd);
    int tam_max = pow(10, tam_max_exp);

    for (int i = 0; i < qtd; i++) {
        vetor.push_back(rand() % tam_max); 
    }
    return vetor;
}

std::vector<float> temperatura (int qtd, int tam_max) {
    std::vector<float> vetor;
    vetor.reserve(qtd);

    for (int i = 0; i < qtd; i++) {
        vetor.push_back(rand() % tam_max); 
    }
    return vetor;
}

PYBIND11_MODULE(robo, m) {
    m.def("criar_sequencia", &criar_sequencia);
    m.def("temperatura", &temperatura);
}