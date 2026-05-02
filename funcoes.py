import random

def rolar_dados(quantidade):
    
    dados_rolados = []
    
    for i in range(quantidade):
        valor = random.randint(1, 6)
        dados_rolados.append(valor)
        
    return dados_rolados

def guardar_dado(dadosrolados, dadosguardados, indice):

    dado = dadosrolados.pop(indice)
    
    dadosguardados.append(dado)
    
    return [dadosrolados, dadosguardados]

def remover_dado(dadosrolados, dadosguardados, indice):
    # remove o dado do estoque
    dado = dadosguardados.pop(indice)
    
    # devolve para os dados rolados
    dadosrolados.append(dado)
    
    # retorna as listas atualizadas
    return [dadosrolados, dadosguardados]

def calcula_pontos_regra_simples(dados):
    
    pontuacao = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for valor in dados:
        pontuacao[valor] += valor
        
    return pontuacao

def calcula_pontos_soma(dados):
    
    somatotal = 0
    
    for valor in dados:
        somatotal += valor
        
    return somatotal

def calcula_pontos_sequencia_baixa(dados):
    
    for inicio in [1, 2, 3]:
        if (inicio in dados and 
            (inicio + 1) in dados and 
            (inicio + 2) in dados and 
            (inicio + 3) in dados):
            return 15
            
    return 0

def calcula_pontos_sequencia_alta(dados):
    
    for inicio in [1, 2]:
        if (inicio in dados and 
            (inicio + 1) in dados and 
            (inicio + 2) in dados and 
            (inicio + 3) in dados and 
            (inicio + 4) in dados):
            return 30
            
    return 0

def calcula_pontos_full_house(dados):
    
    frequencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for valor in dados:
        frequencias[valor] += 1
        
    temtrio = False
    tempar = False
    
    for face in range(1, 7):
        quantidade = frequencias[face]
        if quantidade == 3:
            temtrio = True
        elif quantidade == 2:
            tempar = True
            
    if temtrio and tempar:
        somatotal = 0
        for valordado in dados:
            somatotal += valordado
        return somatotal
        
    return 0

def calcula_pontos_quadra(dados):
    
    frequencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for valor in dados:
        frequencias[valor] += 1
        
    possuiquadra = False
    
    for face in range(1, 7):
        if frequencias[face] >= 4:
            possuiquadra = True
            
    if possuiquadra:
        somatotal = 0
        for valordado in dados:
            somatotal += valordado
        return somatotal
        
    return 0

def calcula_pontos_quina(dados):
    
    frequencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for face_rolada in dados:
        frequencias[face_rolada] += 1
        
    for face in range(1, 7):
        if frequencias[face] >= 5:
            return 50
            
    return 0

def calcula_pontos_regra_avancada(dados):
    
    pontuacao_total = {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }
    
    return pontuacao_total

def faz_jogada(dados, categoria, cartela_de_pontos):
    
    
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancada = calcula_pontos_regra_avancada(dados)
    
    
    if categoria in pontos_avancada:
        
        valor_obtido = pontos_avancada[categoria]
        cartela_de_pontos['regra_avancada'][categoria] = valor_obtido
    else:
        
        categoria_int = int(categoria)
        valor_obtido = pontos_simples[categoria_int]
        cartela_de_pontos['regra_simples'][categoria_int] = valor_obtido
        
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)