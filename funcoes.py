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