print("Digite 1 para pedra, 2 para papel ou 3 para tesoura")
player1 = int(input("Player1: Digite um valor para jogar:"))
player2 = int(input("Player2: Digite um valor para jogar:"))
pedra = 1
papel = 2
tesoura = 3
while player1 != 0 and player2 != 0:
    if player1 == pedra:
        if player2 == pedra:
            print("EMPATE")
        elif player2 == papel:
          print("Player2 venceu")
        elif player2 == tesoura:
            print("Player1 venceu")
    if player1 == papel:
        if player2 == pedra:
            print("PLAYER1 venceu")
        elif player2 == papel:
            print("EMPATE")
        elif player2 == tesoura:
            print("Player2 venceu ")
    if player1 == tesoura:
        if player2 == pedra:
            print("Player2 venceu")
        elif player2 == papel:
            print("PLAYER1 venceu")
        elif player2 == tesoura:
            print("EMPATE")
    player1 = int(input("PLAYER1: Digite um valor para jogar:"))
    player2 = int(input("Player2: Digite um valor para jogar:"))
print("voce saiu do jogo")