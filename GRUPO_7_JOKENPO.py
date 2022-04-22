from random import randint
print('-=-' *20)
print("Bem-vindo ao Jokenpô ")
print(" Digite 1 para jogar com o computador")
print(" Digite 2 para jogar com outro player")
menu = int(input(' Digite um número:'))
print('-=-' *20)
if menu == 1:
       cont_Player = 0
       cont_Computador = 0
       print('Digite 1 para pedra, 2 para papel e 3 para tesoura.')
       Player = int(input('Digite seu numero:'))
       while Player != 0:
              Computador = randint(1, 3)
              if Computador == 1:  # Pedra
                     if Player == 1:
                            print('EMPATE')
                     elif Player == 3:
                            print('JOGADOR VENCE')
                            cont_Player += 1
                     elif Player == 2:
                            print('COMPUTADOR VENCE')
                            cont_Computador += 1
                     else:
                            print('Jogada Inválida')
              elif Computador == 2:  # Papel
                     if Player == 3:
                            print('COMPUTADOR VENCE')
                            cont_Computador += 1
                     elif Player == 2:
                            print('EMPATE')
                     elif Player == 1:
                            print('JOGADOR VENCE')
                            cont_Player += 1
                     else:
                            print('Jogada Inválida')
              elif Computador == 3:  # Tesoura
                     if Player == 2:
                            print('JOGADOR VENCE')
                            cont_Player += 1
                     elif Player == 1:
                            print('COMPUTADOR VENCE')
                            cont_Computador += 1
                     elif Player == 3:
                            print('EMPATE')
                     else:
                            print('Jogada Inválida')
              print("O placar está: %d para você e %d para o computador" % (cont_Player, cont_Computador))
              print('Digite 1 para pedra, 2 para papel e 3 para tesoura.')
              Player = int(input('Digite seu numero:'))
elif menu == 2:
       print("Digite 1 para pedra, 2 para papel ou 3 para tesoura")
       player1 = int(input("Player1: Digite um valor para jogar:"))
       player2 = int(input("Player2: Digite um valor para jogar:"))
       pedra = 1
       papel = 2
       tesoura = 3
       cont_Player1 = 0
       cont_Player2 = 0
       while player1 != 0 and player2 != 0:
              if player1 == pedra:
                     if player2 == pedra:
                            print("EMPATE")
                     elif player2 == papel:
                            print("Player2 venceu")
                            cont_Player2 += 1
                     elif player2 == tesoura:
                            print("Player1 venceu")
                            cont_Player1 += 1
              if player1 == papel:
                     if player2 == pedra:
                            print("PLAYER1 venceu")
                            cont_Player1 += 1
                     elif player2 == papel:
                            print("EMPATE")
                     elif player2 == tesoura:
                            print("Player2 venceu ")
                     cont_Player2 += 1
              if player1 == tesoura:
                     if player2 == pedra:
                            print("Player2 venceu")
                            cont_Player2 += 1
                     elif player2 == papel:
                            print("PLAYER1 venceu")
                            cont_Player1 += 1
                     elif player2 == tesoura:
                            print("EMPATE")
              print("O placar está: %d para PLAYER1 e %d para PLAYER2" % (cont_Player1, cont_Player2))
              player1 = int(input("PLAYER1: Digite um valor para jogar:"))
              player2 = int(input("Player2: Digite um valor para jogar:"))
       print("voce saiu do jogo")
elif menu == 0:
       quit()
