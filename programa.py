from funcoes import calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, calcula_pontos_regra_simples, calcula_pontos_sequencia_alta, calcula_pontos_sequencia_baixa, calcula_pontos_soma, faz_jogada, imprime_cartela, remover_dado, rolar_dados
from funcoes import guardar_dado    


def cria_cartela():
    return {
        'regra_simples': {
            1: -1,
            2: -1,
            3: -1,
            4: -1,
            5: -1,
            6: -1
        },
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }
    }


def imprime_estado_rodada(dados_rolados, dados_guardados):
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")


def combinacao_valida(combinacao, cartela):
    if combinacao in cartela['regra_avancada']:
        return True

    if not combinacao.isdigit():
        return False

    return int(combinacao) in cartela['regra_simples']


def combinacao_utilizada(combinacao, cartela):
    if combinacao in cartela['regra_avancada']:
        return cartela['regra_avancada'][combinacao] != -1

    return cartela['regra_simples'][int(combinacao)] != -1


def calcula_pontuacao_total(cartela):
    pontuacao = 0
    total_simples = 0

    for pontos in cartela['regra_simples'].values():
        total_simples += pontos
        pontuacao += pontos

    for pontos in cartela['regra_avancada'].values():
        pontuacao += pontos

    if total_simples >= 63:
        pontuacao += 35

    return pontuacao


cartela_de_pontos = cria_cartela()
imprime_cartela(cartela_de_pontos)

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    rodada_finalizada = False

    while not rodada_finalizada:
        imprime_estado_rodada(dados_rolados, dados_guardados)
        opcao = input().strip()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            guardar_dado(dados_rolados, dados_guardados, indice)

            if indice >= 0 and indice < len(dados_rolados):
                guardar_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if indice >= 0 and indice < len(dados_guardados):
                remover_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela_de_pontos)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            combinacao = input().strip()

            if not combinacao_valida(combinacao, cartela_de_pontos):
                print("Combinação inválida. Tente novamente.")
            elif combinacao_utilizada(combinacao, cartela_de_pontos):
                print("Essa combinação já foi utilizada.")
            else:
                dados = dados_rolados + dados_guardados
                faz_jogada(dados, combinacao, cartela_de_pontos)
                rodada_finalizada = True

        else:
            print("Opção inválida. Tente novamente.")

imprime_cartela(cartela_de_pontos)
pontuacao = calcula_pontuacao_total(cartela_de_pontos)
print(f"Pontuação total: {pontuacao}")








'''print(rolar_dados(5))

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

print(calcula_pontos_quina([5, 2, 5, 5, 5, 5]))

print(calcula_pontos_quina([5, 2, 5, 5, 2]))


calcula_pontos_regra_avancada([4, 4, 4, 4, 4])

dados = [1, 2, 1, 2, 1]
categoria = "full_house"
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}'''