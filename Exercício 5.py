import random

def jogar_pedra_papel_tesoura():

    vitorias_usuario = 0
    vitorias_maquina = 0
    empates = 0

    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para parar): ").lower()

        if escolha_usuario == 'sair':
            break

        escolhas = ['pedra', 'papel', 'tesoura']
        escolha_maquina = random.choice(escolhas)

        print(f"A máquina escolheu: {escolha_maquina}")

        if escolha_usuario == escolha_maquina:
            print("Empate!")
            empates += 1
        elif (escolha_usuario == 'pedra' and escolha_maquina == 'tesoura') or \
             (escolha_usuario == 'papel' and escolha_maquina == 'pedra') or \
             (escolha_usuario == 'tesoura' and escolha_maquina == 'papel'):
            print("Você venceu!")
            vitorias_usuario += 1
        else:
            print("A máquina venceu!")
            vitorias_maquina += 1

    print("\nResultados finais:")
    print(f"Vitórias do usuário: {vitorias_usuario}")
    print(f"Vitórias da máquina: {vitorias_maquina}")
    print(f"Empates: {empates}")

jogar_pedra_papel_tesoura()