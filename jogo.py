from funcoes import calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_regra_simples, calcula_pontos_sequencia_alta, calcula_pontos_sequencia_baixa, calcula_pontos_soma, remover_dado, rolar_dados
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

print(calcula_pontos_regra_simples([2, 3, 4, 5, 2]))

print(calcula_pontos_soma([2, 3, 4, 5, 2]))

print(calcula_pontos_sequencia_baixa([5, 3, 4, 2, 2]))

print(calcula_pontos_sequencia_baixa([2, 3, 4, 6, 2]))

print(calcula_pontos_sequencia_alta([5, 4, 1, 3, 2, 1]))

print(calcula_pontos_sequencia_alta([2, 3, 4, 6, 2]))

print(calcula_pontos_full_house([5, 2, 5, 5, 2]))

print(calcula_pontos_full_house([5, 5, 5, 5, 2]))

print(calcula_pontos_quadra([5, 2, 5, 5, 5, 1]))

print(calcula_pontos_quadra([5, 2, 5, 5, 2]))
