# Estrutura inicial do sistema
filmes = {
    1: {'nome': 'Filme 1', 'sessoes': {1: {'assentos': 50, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 50},
                                        2: {'assentos': 50, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 50}}},
    2: {'nome': 'Filme 2', 'sessoes': {1: {'assentos': 40, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 40},
                                        2: {'assentos': 40, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 40}}},
    3: {'nome': 'Filme 3', 'sessoes': {1: {'assentos': 30, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 30},
                                        2: {'assentos': 30, 'vendas': {'inteira': 0, 'meia': 0, 'vip': 0}, 'acumulado': {'inteira': 0, 'meia': 0, 'vip': 0}, 'poltronas': ['L'] * 30}}}
}

avaliacoes = {1: None, 2: None, 3: None}

vendas_lanches = {'pipoca': 0, 'refrigerante': 0, 'combo': 0}
precos_lanches = {'pipoca': 10, 'refrigerante': 8, 'combo': 15}

# Funções do sistema
def mostra_poltronas(filme_id, sessao_id):
    sessao = filmes[filme_id]['sessoes'][sessao_id]
    print(f"Poltronas disponíveis para {filmes[filme_id]['nome']} - Sessão {sessao_id}:")
    for i, status in enumerate(sessao['poltronas'], start=1):
        if status == 'L':
            print(f"P{i}", end=" ")
    print()

def vende_poltronas(filme_id, sessao_id, qtde):
    sessao = filmes[filme_id]['sessoes'][sessao_id]
    mostra_poltronas(filme_id, sessao_id)
    cont = 0
    while cont < qtde:
        lugar = input("Escolha o número da poltrona: ")
        if lugar.isdigit() and 1 <= int(lugar) <= len(sessao['poltronas']):
            lugar = int(lugar)
            if sessao['poltronas'][lugar - 1] == 'L':
                sessao['poltronas'][lugar - 1] = 'O'
                cont += 1
                print(f"Poltrona {lugar} reservada com sucesso!")
            else:
                print("Poltrona ocupada! Escolha outra.")
        else:
            print("Número de poltrona inválido. Tente novamente.")
    mostra_poltronas(filme_id, sessao_id)

def vender_lanches():
    print("Lanches disponíveis:")
    print("1 - Pipoca (R$10)")
    print("2 - Refrigerante (R$8)")
    print("3 - Combo (Pipoca + Refrigerante, R$15)")
    print("4 - Voltar")
    escolha = input("Escolha um lanche: ")
    while escolha not in ['1', '2', '3', '4']:
        escolha = input("Opção inválida. Escolha novamente: ")

    if escolha == '4':
        return
    lanches = {1: 'pipoca', 2: 'refrigerante', 3: 'combo'}
    lanche = lanches[int(escolha)]
    quantidade = input(f"Quantos {lanche}s deseja comprar? ")
    while not quantidade.isdigit() or int(quantidade) <= 0:
        quantidade = input("Quantidade inválida. Digite novamente: ")
    quantidade = int(quantidade)
    vendas_lanches[lanche] += quantidade
    print(f"{quantidade} {lanche}(s) adicionados ao pedido!")

def comprar_ingresso(filme_id, sessao_id):
    sessao = filmes[filme_id]['sessoes'][sessao_id]
    if sessao['assentos'] <= 0:
        print('Sessão esgotada! Escolha outro filme ou sessão.')
        return
    
    print(f"{sessao['assentos']} assentos disponíveis.")
    print("1 - Inteira (R$20)")
    print("2 - Meia (R$10)")
    print("3 - VIP (R$30)")
    tipo = input("Escolha o tipo de ingresso: ")
    while tipo not in ['1', '2', '3']:
        tipo = input("Opção inválida. Escolha novamente: ")

    tipos_ingresso = {1: ('inteira', 20), 2: ('meia', 10), 3: ('vip', 30)}
    tipo_ingresso, preco = tipos_ingresso[int(tipo)]

    quantidade = input(f"Quantos ingressos {tipo_ingresso} deseja comprar? ")
    while not quantidade.isdigit() or int(quantidade) <= 0 or int(quantidade) > sessao['assentos']:
        quantidade = input("Quantidade inválida. Digite novamente: ")
    quantidade = int(quantidade)

    sessao['vendas'][tipo_ingresso] += quantidade
    sessao['assentos'] -= quantidade
    sessao['acumulado'][tipo_ingresso] += quantidade * preco
    print(f"Compra realizada. Total: R${quantidade * preco:.2f}")
    vende_poltronas(filme_id, sessao_id, quantidade)

def avaliar_filme(filme_id):
    nota = input("Dê sua nota (1 a 3): ")
    while nota not in ['1', '2', '3']:
        nota = input("Nota inválida. Digite novamente: ")
    avaliacoes[filme_id] = int(nota)
    print(f"Filme avaliado com nota {nota}!")

def exibir_relatorio():
    print("\n=== Relatório de Vendas de Ingressos ===")
    for filme_id, filme in filmes.items():
        print(f"Filme: {filme['nome']}")
        for sessao_id, sessao in filme['sessoes'].items():
            print(f"  Sessão {sessao_id}:")
            for tipo, quantidade in sessao['vendas'].items():
                print(f"    {tipo.capitalize()}: {quantidade} vendidos - Total: R${sessao['acumulado'][tipo]:.2f}")

    print("\n=== Relatório de Vendas de Lanches ===")
    for lanche, quantidade in vendas_lanches.items():
        print(f"{lanche.capitalize()}: {quantidade} vendidos - Total: R${quantidade * precos_lanches[lanche]:.2f}")

    print("\n=== Relatório de Avaliações ===")
    for filme_id, nota in avaliacoes.items():
        print(f"Filme: {filmes[filme_id]['nome']} - Nota: {nota if nota else 'Não avaliado'}")

# Programa principal
while True:
    print('Seja Bem- Vindo ao CineMack!Segue o menu abaixo:')
    print("\n1 - Comprar ingressos para Filme 1 - Sessão 1")
    print("2 - Comprar ingressos para Filme 1 - Sessão 2")
    print("3 - Comprar ingressos para Filme 2 - Sessão 1")
    print("4 - Comprar ingressos para Filme 2 - Sessão 2")
    print("5 - Comprar ingressos para Filme 3 - Sessão 1")
    print("6 - Comprar ingressos para Filme 3 - Sessão 2")
    print("7 - Avaliar um filme")
    print("8 - Encerrar o dia e exibir o relatório")
    print("9 - Comprar lanches")

    opcao = input("Escolha uma opção: ")
    while opcao not in [str(i) for i in range(1, 10)]:
        opcao = input("Opção inválida. Escolha uma opção válida (1-9): ")

    if opcao == '8':
        exibir_relatorio()
        break
    elif opcao in ['1', '2', '3', '4', '5', '6']:
        filme_id = (int(opcao) - 1) // 2 + 1
        sessao_id = 1 if int(opcao) % 2 != 0 else 2
        comprar_ingresso(filme_id, sessao_id)
    elif opcao == '7':
        filme_id = input("Escolha o filme (1, 2 ou 3): ")
        while filme_id not in ['1', '2', '3']:
            filme_id = input("Filme inválido. Escolha novamente (1, 2 ou 3): ")
        avaliar_filme(int(filme_id))
    elif opcao == '9':
        vender_lanches()

