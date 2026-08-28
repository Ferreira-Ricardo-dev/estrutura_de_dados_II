import robo
import blubble_sort
import quick_sort
import robo

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

qtd = int(input("Digite a quantidade de elementos: "))
tam_max = int(input("Digite o valor máximo (expoente de 10): "))

while True:
    try:
        opcao = int(input("""\nEscolhas uma das opções a seguir:
        \n1 - Gerar Sequência
        \n2 - Gerar Sequência de Temperatura
        \n3 - Ordenar com Bubble Sort
        \n4 - Ordenar com Quick Sort\n"""))

        if opcao == 1:
            print("\n--- Gerando Sequência via C++ ---")
            # O C++ retorna uma lista Python perfeita
            vetor_original = robo.criar_sequencia(qtd, tam_max)
            print(f"Original: {vetor_original}")
            break

        elif opcao == 2:
            print("\n--- Gerando Sequência temperatura via C++ ---")
            vetor_temperatura = robo.temperatura(qtd, tam_max)
            print(f"Temperatura: {vetor_temperatura}")
            break

        elif opcao == 3:
            print("\n--- Ordenando com Bubble Sort (C++) ---")
            vetor_bubble = blubble_sort.bubble_sort(vetor_original)
            print(f"Bubble: {vetor_bubble}")
            break

        elif opcao == 4:
            print("\n--- Ordenando com Quick Sort (C++) ---")
            vetor_quick = quick_sort.quick_sort(vetor_original)
            print(f"Quick: {vetor_quick}")
            break

        else:
            print("Valor inválido, escolha um opção válida de 1 a 4!")
            continue
    except ValueError:
        print("Valor inválido, escolha um opção válida de 1 a 4!")
        continue
 
        