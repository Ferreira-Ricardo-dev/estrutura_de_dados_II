from estrutura_de_dados_II.Robô.robo import *
import blubble_sort
import quick_sort

while True:
    try:
        opcao = int(input("""\nEscolhas uma das opções a seguir:
1 - Usar algoritmos de busca Bubble Sort e Quick Sort
2 - Teste de busca em matrizes
3 - Investigação do array de temperaturas
4 - Monitoramento de Sensores com Matrizes
5 - Sair\n"""))

        if opcao == 1:
            array_base = create_array()
            print(f"\nArray Padrão Aleatório: {array_base}\n")
            print("\nEscolha uma das opções a seguir")
            while True:
                try:
                    opcao_1 = int(input("""
1 - Experimentar ordenação por Bubble Sort
2 - Experimentar ordenação por Quick Sort
3 - Definir um novo tamanho de array
4 - Voltar\n"""))

                    if opcao_1 == 1:
                        array_bubble = blubble_sort.bubble_sort(array_base)
                        print(f"Blubble: {array_bubble}")
                        continue

                    elif opcao_1 == 2:
                        array_quick = quick_sort.quick_sort(array_base)
                        print(f"Quick: {array_quick}")
                        continue

                    elif opcao_1 == 3: 
                        size = int(input("Digite o tamanho do novo array: "))
                        array_base = create_array(size)
                        print(f"\nNovo Array de tamanho {size}: {array_base}\n")
                        continue

                    elif opcao_1 == 4:
                        break

                    else:
                        print("Valor inválido, escolha um opção válida de 1 a 4!")
                        continue

                except ValueError:
                    print("Valor inválido, escolha um opção válida de 1 a 4!")
                    continue

        elif opcao == 2:
            matriz_base = create_matriz_ordenada(2, 2)
            print(f"\nMatriz Padrão 2x2:")
            show_matriz(matriz_base)
            print("\nEscolha uma das opções a seguir")
            while True:
                try:
                    opcao_1 = int(input("""
1 - Buscar elemento na matriz
2 - Definir nova dimensão para matriz
3 - Voltar\n"""))
            
                    if opcao_1 == 1:
                        valor_pesquisado = int(input("Digite um valor para pesquisar na matriz: "))
                        print(buscar_valor_matriz(matriz_base, valor_pesquisado))
                        continue

                    elif opcao_1 == 2:
                        size = int(input("Digite a dimensão da nova matriz: "))
                        matriz_base = create_matriz_ordenada(size, size)
                        print(f"\nNova Matriz {size}x{size}:")
                        show_matriz(matriz_base)
                        continue

                    elif opcao_1 == 3:
                        break

                    else:
                        print("Valor inválido, escolha um opção válida de 1 a 3!")
                        continue

                except ValueError:
                    print("Valor inválido, escolha um opção válida de 1 a 3!")
                    continue

        elif opcao == 3:
            temperaturas = create_array_temperatura()
            print(f"Temperaturas Aleatórias de 0ºC até 45ºC: {temperaturas}")
            relatorio = analisar_temperaturas(temperaturas)
            print(relatorio)
            continue

        elif opcao == 4:
            matriz_sensores = create_matriz_sensores()
            show_matriz_sensores(matriz_sensores)
            limite = float(input("\nDigite o limite de temperatura: "))
            relatorio_sensores = analisar_temperaturas_sensores(matriz_sensores, limite=limite)
            print(relatorio_sensores)
            continue

        elif opcao == 5:
            print("Obrigado por testar nosso código ;-)")
            print("Encerrando...")
            break

        else:
            print("Valor inválido, escolha um opção válida de 1 a 4!")
            continue
    except ValueError:
        print("Valor inválido, escolha um opção válida de 1 a 4!")
        continue
 
        