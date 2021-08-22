from random import randint

print ('\n--- JO KEN PO ---\n')
acoes_do_jogo = ('','Pedra', 'Papel', 'Tesoura')
bot = randint (1,3)
print (' [1] Pedra\n [2] Papel\n [3] Tesoura\n')
jogador = int(input('Qual é sua jogada? '))
print ('\nRobô jogou {}'.format(acoes_do_jogo[bot]))
print ('Você jogou {}'.format(acoes_do_jogo[jogador]))

#add regras do jogo
if bot ==1 and jogador == 2:
    print ('VOCÊ GANHOU!')
elif bot ==2 and jogador ==1:
    print ('VOCÊ PERDEU!')
elif bot ==3 and jogador ==1:
    print ('VOCÊ GANHOU!')
elif bot ==1 and jogador == 3:
    print ('VOCÊ PERDEU!')
elif bot ==2 and jogador ==3:
    print ('VOCÊ GANHOU!')
elif bot ==3 and jogador ==2:
    print ('VOCÊ PERDEU!')
elif bot == jogador:
    print ('EMPATOU!')
