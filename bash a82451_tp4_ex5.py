# a82451
# Tp4
# Exe 05

LINHAS_TABULEIRO = 7
COLUNAS_TABULEIRO = 7
tabuleiro = [
    ["-" for i in range(LINHAS_TABULEIRO)] for i in range(COLUNAS_TABULEIRO)
]  # Um array de arrays a serem preenchidos
jogadores = ["X", "O"]
break_loop = False
resultado = False


def jogada(coluna, jogador):
    coluna = coluna - 1  # Internamente colunas vão de 0 a 6 e não de 1 a 7

    while (
        coluna not in range(0, 7) or tabuleiro[0][coluna] != "-"
    ):  # Mecanismo para aceitar apenas colunas de 1 a 7
        # ou se a casa da linha do topo desta coluna está livre

        coluna = (
            int(input(f"Jogada inválida! Jogador {jogador}, escolha outra posição: "))
            - 1
        )  # Sem este -1, caso o usuário colocasse 5, ele iria na coluna 6, pois vamos de 0 a 6

    for linha in range(
        LINHAS_TABULEIRO - 1, -1, -1
    ):  # Começamos do fundo até o index (que é o topo), escalando de -1 em -1
        if tabuleiro[linha][coluna] == "-":
            tabuleiro[linha][coluna] = jogadores[jogador - 1]
            break

        # Se o if não for satisfeito, voltaremos ao for,
        # onde ao inves de 6 (LINHAS_TABULEIRO - 1), será 5 (LINHAS_TABULEIRO - 1 - 1)


def print_Tabuleiro():
    """Printa o tabuleiro, com um join separada cada casa de cada linha e um divisor de linhas"""

    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 26)


def win_Diagnoal() -> bool:
    """Valida se há diagonais iguais"""

    # Para se calcular diagonais para o canto superior direito, usamos a fórmula:
    # (linha, coluna), (linha - 1, coluna + 1), (linha - 2, coluna + 2), (linha - 3, coluna + 3)
    # Pois uma diagonal assim, sobe, avança em linha e coluna

    for linha in range(3, LINHAS_TABULEIRO):
        for coluna in range(0, 4):
            if tabuleiro[linha][coluna] != "-":  # Não procuramos por diagonais vazias
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha - 1][coluna + 1]
                    == tabuleiro[linha - 2][coluna + 2]
                    == tabuleiro[linha - 3][coluna + 3]
                ):
                    return True

    # Para se calcular diagonais para o canto inferior direito, usamos a fórmula:
    # (linha, coluna), (linha + 1, coluna + 1), (linha + 2, coluna + 2), (linha + 3, coluna + 3)
    # Pois uma diagonal assim, desce, diminui em linha e aumenta em coluna

    for linha in range(0, 4):
        for coluna in range(0, 4):
            if tabuleiro[linha][coluna] != "-":  # Não procuramos por diagonais vazias
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha + 1][coluna + 1]
                    == tabuleiro[linha + 2][coluna + 2]
                    == tabuleiro[linha + 3][coluna + 3]
                ):
                    return True

    return False


def win_Horizontal() -> bool:
    """Valida se há horizontais iguais"""

    for linha in range(0, LINHAS_TABULEIRO):
        for coluna in range(0, 4):
            if tabuleiro[linha][coluna] != "-":  # Não procuramos por horizontais vazias
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha][coluna + 1]
                    == tabuleiro[linha][coluna + 2]
                    == tabuleiro[linha][coluna + 3]
                ):
                    return True

        for coluna in range(6, 2, -1):
            if tabuleiro[linha][coluna] != "-":
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha][coluna - 1]
                    == tabuleiro[linha][coluna - 2]
                    == tabuleiro[linha][coluna - 3]
                ):
                    return True

    return False


def win_Vertical() -> bool:
    """Verifica se há linhas verticais iguais"""

    for linha in range(0, 4):
        for coluna in range(0, COLUNAS_TABULEIRO):
            if tabuleiro[linha][coluna] != "-":  # Não procuramos por verticais vazias
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha + 1][coluna]
                    == tabuleiro[linha + 2][coluna]
                    == tabuleiro[linha + 3][coluna]
                ):
                    return True

        for coluna in range(6, 2, -1):
            if tabuleiro[linha][coluna] != "-":
                if (
                    tabuleiro[linha][coluna]
                    == tabuleiro[linha + 1][coluna]
                    == tabuleiro[linha + 2][coluna]
                    == tabuleiro[linha + 3][coluna]
                ):
                    return True

    return False


def win() -> bool:
    """Executa todas as funções win"""

    if win_Diagnoal():
        return True

    elif win_Horizontal():
        return True

    elif win_Vertical():
        return True

    return False


def empate() -> bool:
    contador_Empate = 0

    for linha in tabuleiro:
        contador_Empate = contador_Empate + linha.count("-")

    if contador_Empate == 0:
        return True

    else:
        return False


print("-" * 27)
print("-> |Vamos Jogar Liga 4| <-")
print("-" * 27)
print_Tabuleiro()
while True:
    for vez in range(
        LINHAS_TABULEIRO * COLUNAS_TABULEIRO
    ):  # Quantas vezes são possíveis de serem jogadas, sete colunas e sete linhas
        for i in range(1, 3):
            posicao = int(
                input(f"Jogador {i}, é a sua vez, selecione uma coluna (1-7): ")
            )
            print("-" * 26)
            jogada(posicao, i)
            print_Tabuleiro()

            if win():
                resultado = True
                print(f"O jogador {i} venceu!")
                print("-" * 18)
                print("-> |Fim de Jogo| <-")
                print("-" * 18)
                break_loop = True
                break

            elif empate():
                resultado = True
                print("As Casas Acabaram! Empate!")
                print("-" * 18)
                print("-> |Fim de Jogo| <-")
                print("-" * 18)
                break_loop = True
                break

        if resultado == True:
            break

    if resultado == True:
        break
