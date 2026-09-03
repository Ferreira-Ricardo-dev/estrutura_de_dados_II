from Robô.robo import create_array_temperatura

#Recebendo as 10 temperaturas
temperaturas = create_array_temperatura()

#Mostrando elementos armazenados
print(f"Temperaturas: {temperaturas}")

#Inicializando variáveis
media = 0
soma = 0
maior_valor = temperaturas[0]
indice_maior_valor = 0
menor_valor = temperaturas[0]
indice_menor_valor = 0

#Fazendo as operações
for i in range(10):
    soma += temperaturas[i]

    if temperaturas[i] > maior_valor:
        maior_valor = temperaturas[i]
        indice_maior_valor = i

    if temperaturas[i] < menor_valor:
        menor_valor = temperaturas[i]
        indice_menor_valor = i

media = soma / len(temperaturas)

#Mostrando resultados
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior_valor:.2f}")
print(f"Menor valor: {menor_valor:.2f}")
print(f"Índice do maior valor: {indice_maior_valor:.0f}")
print(f"Índice do menor valor: {indice_menor_valor:.0f}")