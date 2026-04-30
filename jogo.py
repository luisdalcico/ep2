from funcoes import remover_dado, rolar_dados
from funcoes import guardar_dado    

print(rolar_dados(5))

dados_rolados = [1, 3, 2]
dados_no_estoque = [1, 2]
dado_para_guardar = 1

print(guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar))

dados_rolados = [2, 2, 2, 2]
dados_no_estoque = [1]
dado_para_remover = 0

print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))