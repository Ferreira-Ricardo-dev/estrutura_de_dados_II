#Arquivo que vai conter os funções necessárias para criar uma matriz personalizada pelo usuário

def create_matriz_ordenada(a=1, b=1):
    """Função que monta e retorna uma matriz ordenada, para isso, ela recebe 
    duas variáveis inteiras 'a' e 'b' que representam respectivamente
    as linhas e colunas da matriz, dada as dimensões a função monta uma matriz
    ordenada iniciando de 1 a n."""
    matriz = []
    valor = 0
    for i in range(a):
        linha = []
        for j in range(b):
            valor += 1
            linha.append(valor)

        matriz.append(linha)

    return matriz

def show_matriz(matriz):
    """Função que mostra todos os elementos de uma 
    matriz de maneira formatada."""
    for linha in matriz:
        print(linha)

def create_matriz_aleatoria(a=1, b=1, n=1000):
    """Função que monta e retorna uma matriz aleatória, para isso, ela recebe 
        duas variáveis inteiras 'a' e 'b' que representam respectivamente
        as linhas e colunas da matriz, dada as dimensões a função monta uma matriz
        aleatória iniciando de 1 a n, sendo n o valor máximo possível da matriz."""
    try:
        import random
    except ImportError:
        print("Erro de importação de biblioteca!")
    else:
        matriz = []
        valor = 0
        for i in range(a):
            linha = []
            for j in range(b):
                valor = random.randrange(n)
                linha.append(valor)
    
            matriz.append(linha)
        
        return matriz

def create_array_temperatura(a=10, min=0.0, max=45.0):
    """Função que cria um array de temperaturas aleatórias."""
    try:
        import random
    except ImportError:
        print("Erro de importação de biblioteca!")
    else:
        temperaturas = []
        for i in range(a):
            temperatura = round(random.uniform(min, max), 2)
            temperaturas.append(temperatura)

    return temperaturas

if __name__ == '__main__':
    matriz = create_matriz_ordenada(10, 10)
    show_matriz(matriz)
    matriz_1 = create_matriz_aleatoria(5, 5)
    show_matriz(matriz_1)
    temperaturas = create_array_temperatura()
    print(temperaturas)