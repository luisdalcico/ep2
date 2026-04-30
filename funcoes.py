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