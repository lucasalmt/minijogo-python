import random

player_score = 0
rounds_played = 0

while True:
    
    options = ["pedra", "papel", "tesoura"]

    # Solicita a entrada do jogador e a converte para letras minúsculas para garantir a consistência.
    player_choice = input("Escolha uma opção (pedra, papel, tesoura): ").lower()

    # Verifica se a escolha do jogador é uma das opções válidas,
    # se não for, informa o usuário e pula para a próxima iteração do loop.
    if player_choice not in options:
        print("Opção inválida! Por favor, tente novamente.")
        continue

    # O computador seleciona aleatoriamente uma das opções da lista.
    computer_choice = random.choice(options)
    print(f"O computador escolheu: {computer_choice}")

    rounds_played += 1

    # Compara as escolhas para determinar o resultado da rodada.
    # Caso de empate.
    if player_choice == computer_choice:
        print("É um empate!")
    # Casos em que o jogador vence.
    elif (player_choice == "pedra" and computer_choice == "tesoura") or \
         (player_choice == "tesoura" and computer_choice == "papel") or \
         (player_choice == "papel" and computer_choice == "pedra"):
        print("Você venceu a rodada!")
        # Incrementa a pontuação do jogador se ele vencer.
        player_score += 1
    # Se não for empate nem vitória do jogador, o computador vence.
    else:
        print("Você perdeu a rodada!")

    play_again = input("Você quer jogar novamente? (s/n): ").lower()


    if play_again != "s":
        break

print("\n--- Fim do Jogo ---")
print(f"Você jogou {rounds_played} rodadas.")
print(f"Sua pontuação final é: {player_score} vitórias.")
print("Obrigado por jogar!")