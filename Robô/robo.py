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

def create_array(a=10):
    """Função que cria um array com valores aleatórios."""
    try:
        import random
    except ImportError:
        print("Erro de importação de biblioteca!")
    else:
        array = []
        for i in range(a):
            element = random.randint(1, a)
            array.append(element)

    return array

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


def analisar_temperaturas(temperaturas):
    """Função que analisa um array de dados de temperaturas.
       Recebe o array 'temperaturas' e um valor float 'limite'. 
       Calcula a média, identifica o maior/menor valor com seus respectivos 
       índices."""
    try:
        total_leituras = len(temperaturas)
        if total_leituras == 0:
            raise IndexError
    except (IndexError, TypeError):
        return "Erro: O array de temperaturas enviado está inválido ou vazio."
    else:
        soma = 0
        maior_valor = temperaturas[0]
        indice_maior_valor = 0
        menor_valor = temperaturas[0]
        indice_menor_valor = 0
        quantidade_acima = 0
        
        relatorio = f"Temperaturas analisadas: {temperaturas}\n\n"
        
        for i in range(total_leituras):
            soma += temperaturas[i]
            
            if temperaturas[i] > maior_valor:
                maior_valor = temperaturas[i]
                indice_maior_valor = i
                
            if temperaturas[i] < menor_valor:
                menor_valor = temperaturas[i]
                indice_menor_valor = i

        media = soma / total_leituras
        
        relatorio += f"Média: {media:.2f} °C\n"
        relatorio += f"Maior valor: {maior_valor:.2f} °C (Índice: {indice_maior_valor})\n"
        relatorio += f"Menor valor: {menor_valor:.2f} °C (Índice: {indice_menor_valor})\n\n"
        
        return relatorio

def buscar_valor_matriz(matriz, valor):
    contador_comparacao = 0
    encontrado = False
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            contador_comparacao += 1
            if matriz[linha][coluna] == valor:
                encontrado = True
                return f"\nO valor {valor} foi encontrado na linha {linha} e coluna {coluna} \nForam necessárias {contador_comparacao} comparações para encontrar o valor"
            
    if not encontrado:
        return f"O valor {valor} não foi encontrado na matriz."

def create_matriz_sensores(total_sensores=5, total_horas=24, temp_min=20.0, temp_max=40.0):
    """Função que monta e retorna uma matriz simulando dados de sensores de temperatura.
        Recebe a quantidade de 'total_sensores' (linhas), 'total_horas' (colunas)
        e os limites 'temp_min' e 'temp_max' para gerar valores decimais (float)
        aleatórios simulando as leituras de temperatura."""
    try:
        import random
    except ImportError:
        print("Erro de importação de biblioteca!")
    else:
        matriz_sensores = []
        for i in range(total_sensores):
            linha = []
            for j in range(total_horas):
                # Gera um número decimal (float) entre a temperatura mínima e máxima
                leitura = random.uniform(temp_min, temp_max)
                linha.append(leitura)
                
            matriz_sensores.append(linha)
            
        return matriz_sensores

def show_matriz_sensores(matriz):
    """Função que mostra todos os elementos da
    matriz de sensores de maneira formatada."""
    for i, linha in enumerate(matriz):
        # Identifica o número do sensor (linha)
        print(f"Sensor {i + 1}: ", end="")
        
        # Formata cada temperatura da linha com 2 casas decimais e espaçamento de 7 caracteres
        for temperatura in linha:
            print(f"{temperatura:7.2f}°C", end="")
            
        print() # Quebra de linha ao final de cada sensor


def analisar_temperaturas_sensores(sensores, limite):
    """Função que analisa uma matriz de dados de sensores de temperatura. 
       Recebe a matriz 'sensores' (linhas = sensores, colunas = horários) 
       e um valor float 'limite'. Calcula médias, identifica a maior 
       temperatura e mapeia as ocorrências que ultrapassaram o limite, 
       retornando um relatório completo em formato de texto."""
    try:
        total_sensores = len(sensores)
        total_horarios = len(sensores[0]) if total_sensores > 0 else 0
    except IndexError:
        return "Erro: A matriz de sensores enviada está inválida ou vazia."
    else:
        maior_temperatura = sensores[0][0]
        sensor_maior = 0
        horario_maior = 0
        soma_geral = 0
        quantidade_acima = 0
        
        relatorio = ""
        
        for i in range(total_sensores):
            soma_sensor = 0
            for j in range(total_horarios):
                soma_sensor += sensores[i][j]
                soma_geral += sensores[i][j]

                if sensores[i][j] > maior_temperatura:
                    maior_temperatura = sensores[i][j]
                    sensor_maior = i
                    horario_maior = j

            media_sensor = soma_sensor / total_horarios
            relatorio += f"Média do Sensor {i + 1}: {media_sensor:.2f} °C\n"

        media_geral = soma_geral / (total_sensores * total_horarios)
        relatorio += f"\nMédia geral: {media_geral:.2f} °C\n\n"
        
        relatorio += f"Maior temperatura: {maior_temperatura:.2f} °C\n"
        relatorio += f"Sensor responsável: Sensor {sensor_maior + 1}\n"
        relatorio += f"Horário da ocorrência: {horario_maior} horas\n\n"

        relatorio += f"--- Leituras acima de {limite} °C ---\n"
        for i in range(total_sensores):
            sensor_impresso = False
            for j in range(total_horarios):
                if sensores[i][j] > limite:
                    quantidade_acima += 1
                    if not sensor_impresso:
                        relatorio += f"Sensor {i + 1}:\n"
                        sensor_impresso = True
                    relatorio += f"  - Horário: {j} horas\n"

        relatorio += f"\nQuantidade total de leituras acima do limite: {quantidade_acima}"
        
        return relatorio


if __name__ == '__main__':
    temperaturas = create_array_temperatura()
    print(temperaturas)
    relatorio = analisar_temperaturas(temperaturas)
    print(relatorio)