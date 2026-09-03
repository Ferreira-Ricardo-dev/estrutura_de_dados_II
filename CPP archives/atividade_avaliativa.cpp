#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pybind11/pybind11.h>

void criar_sequencia();
void clonar_vetor(int vetor[], int qtd);
void bubble_sort(int vetor[], int qtd);
void quick_sort(int vetor[], int qtd);
void quick_sort_recursivo(int vetor[], int i, int s);
void mostrar_vetor();
void comparar_bubble_quick(int vetor[], int qtd);
void desorganizar_vetor();

struct AlgoritimoMetricas {
    int comparacoes;
    int trocas;
    int movimentacoes;
    double tempo;
};

struct {
    AlgoritimoMetricas bubble;
    AlgoritimoMetricas quick;
} metricas;

int qtd, *vetor, aux, *vetorAuxBubble, *vetorAuxQuick;

int main() {
    int opcao;
    char continuar;

    do {
        printf("\nEscolha a opcao desejada:\n");
        printf("1 Criar sequencia \n");
        printf("2 Bublle Sort \n");
        printf("3 Quick Sort \n");
        printf("4 Mostrar vetor \n");
        printf("5 Comparar bubble X quick \n");
        printf("6 Desorganizar vetor \n");
        printf("7 Sair \n");
        scanf(" %d", &opcao);

        switch (opcao) {
            case 1:
                printf("\nCriar sequencia\n");
                criar_sequencia();
                clonar_vetor(vetor, qtd);
                break;
            case 2:
                if (vetor == NULL) {
                    printf("\nVetor nao criado. Crie uma sequencia primeiro.\n");
                    break;
                }
                printf("\nBublle Sort\n");
                bubble_sort(vetor, qtd);
                printf("trocas: %d", metricas.bubble.trocas);
                printf("\n Tempo gasto: %.2f ms\n", metricas.bubble.tempo);
                break;
            case 3:
                if (vetor == NULL) {
                    printf("\nVetor nao criado. Crie uma sequencia primeiro.\n");
                    break;
                }
                printf("\nQuick Sort\n");
                quick_sort(vetor, qtd );
                printf("trocas: %d", metricas.quick.trocas);
                printf("\n Tempo gasto: %.2f ms\n", metricas.quick.tempo);
                break;
            case 4:
                if (vetor == NULL) {
                    printf("\nVetor nao criado. Crie uma sequencia primeiro.\n");
                    break;
                }
                printf("\nMostrar vetor\n");
                mostrar_vetor();
                break;
            case 5:
                if (vetor == NULL) {
                    printf("\nVetor nao criado. Crie uma sequencia primeiro.\n");
                    break;
                }
                printf("\n Comparar bubble X quick\n");
                comparar_bubble_quick(vetor, qtd);
                break;
            case 6:
                printf("\nDesorganizando vetor\n");
                desorganizar_vetor();
                break;
            case 7:
                printf("\nSaindo do programa\n");
                break;
            default:
                printf("\nOpcao invalida\n");   
        }
        if (opcao != 7) {
            printf("\nDeseja continuar? (s/n): ");
            scanf(" %c", &continuar);
        }
    } while (opcao != 7 and (continuar == 's' or continuar == 'S'));           
}    
void criar_sequencia() {
    if (vetor != NULL) {
        free(vetor);
    }
    printf("Digite a quantidade de elementos: ");
    scanf("%d", &qtd);
    vetor = (int*)malloc(qtd * sizeof(int)); 
    for (int i = 0; i < qtd; i++) {
        vetor[i] = rand() % 10000; 
    }
}
void clonar_vetor(int vetor[], int qtd) {
    vetorAuxBubble = (int*)malloc(qtd * sizeof(int));
    vetorAuxQuick = (int*)malloc(qtd * sizeof(int));
    for (int i = 0; i < qtd; i++) {
        vetorAuxBubble[i] = vetor[i];
        vetorAuxQuick[i] = vetor[i];
    } 
}
void bubble_sort(int vetorAuxBubble[], int qtd) { 
    metricas.bubble.trocas = 0;
    metricas.bubble.comparacoes = 0;
    metricas.bubble.movimentacoes = 0;

    clock_t start = clock();
    
     for (int i = 0; i< qtd - 1; i++) { 
        for (int j = 0; j < qtd - 1 - i; j++) { 
            metricas.bubble.comparacoes++;
            if (vetorAuxBubble[j] > vetorAuxBubble[j + 1]) { 
                aux = vetorAuxBubble[j];
                vetorAuxBubble[j] = vetorAuxBubble[j + 1];
                vetorAuxBubble[j + 1] = aux;
                metricas.bubble.trocas++;
                metricas.bubble.movimentacoes += 3;
            }
        }
    }

    clock_t end = clock();
    metricas.bubble.tempo = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;
    
}
void quick_sort(int vetorAuxQuick[], int qtd) {
    metricas.quick.trocas = 0;
    metricas.quick.comparacoes = 0;
    metricas.quick.movimentacoes = 0;

    clock_t start = clock();
    quick_sort_recursivo(vetorAuxQuick, 0, qtd - 1);
    clock_t end = clock();
    metricas.quick.tempo = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;
} 
void quick_sort_recursivo(int vetorAuxQuick[], int i, int s) {
    int esq = i, dir = s;
    int pivo = vetorAuxQuick[(i + s) / 2];
    metricas.quick.movimentacoes++;
    
    while (esq <= dir) {
        metricas.quick.comparacoes++;
        while (vetorAuxQuick[esq] < pivo) {
            esq++;
            metricas.quick.comparacoes++;
        }
        while (vetorAuxQuick[dir] > pivo) {
            dir--;
            metricas.quick.comparacoes++;
        }
        if (esq <= dir) {
            if (esq != dir) {
                aux = vetorAuxQuick[esq];
                vetorAuxQuick[esq] = vetorAuxQuick[dir];
                vetorAuxQuick[dir] = aux;
                metricas.quick.trocas++;
                metricas.quick.movimentacoes += 3;
            }
            esq++;
            dir--;     
        }
    }
    if (i < dir) quick_sort_recursivo(vetorAuxQuick, i, dir);
    if (esq < s) quick_sort_recursivo(vetorAuxQuick, esq, s);
}
void mostrar_vetor() {
    printf("\nVetor: ");
    for (int i = 0; i < qtd; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}
void comparar_bubble_quick(int vetor[], int qtd){
    printf("\nComparando Bubble Sort e Quick Sort\n");
    printf("Vetor original: ");
    mostrar_vetor();
    clonar_vetor(vetor, qtd);
    bubble_sort(vetorAuxBubble, qtd);
    printf("\nBubble Sort - Trocas: %d\n", metricas.bubble.trocas);
    printf("\nTempo gasto: %.2f ms\n", metricas.bubble.tempo);
    printf("Comparacoes: %d\n", metricas.bubble.comparacoes);
    printf("Movimentacoes: %d\n", metricas.bubble.movimentacoes);
    printf("\n");
    printf("Vetor: ");
    for (int i = 0; i < qtd; i++) {
        printf("%d ", vetorAuxBubble[i]);
    }
    printf("\n");
    quick_sort(vetorAuxQuick, qtd);
    printf("\nQuick Sort - Trocas: %d\n", metricas.quick.trocas);
    printf("\nTempo gasto: %.2f ms\n", metricas.quick.tempo);
    printf("Comparacoes: %d\n", metricas.quick.comparacoes);
    printf("Movimentacoes: %d\n", metricas.quick.movimentacoes);
    printf("Vetor: ");
    for (int i = 0; i < qtd; i++) {
        printf("%d ", vetorAuxQuick[i]);
    }
} 
void desorganizar_vetor() {
    for (int i = 0; i < qtd; i++) {
        int pos1 = rand() % qtd; // gera um numero aleatorio entre 0 e qtd-1
        int pos2 = rand() % qtd; // gera um numero aleatorio entre 0 e qtd-1
        aux = vetor[pos1];
        vetor[pos1] = vetor[pos2];
        vetor[pos2] = aux;
    }
}