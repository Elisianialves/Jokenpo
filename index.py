from random import randint
from time import sleep

# boas vindas
print ('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print ('                     VAMOS JOGAR JOKENPO                            ')
print ('Pedra ganha de Tesoura, Tesoura ganha de Papel, Papel ganha de Pedra')
print ('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n')
nome = input('Qual seu nome? ').capitalize()
sleep (1)
print ('{} Bem-Vindo(a) ao Jogo'.format(nome))
sleep (1)

# jogo
acoes_do_jogo = ('','Pedra', 'Papel', 'Tesoura', 'Sair')
bot = randint (1,3)
print ('\nEscolha sua opção:')
print (' [1] Pedra\n [2] Papel\n [3] Tesoura\n')
print ('OU APERTE 4 PARA SAIR\n ')
sleep (1)
jogador = int(input('Qual é sua jogada? '))
while jogador not in (1,2,3,4):
    jogador = int (
        input('JOGADA INVÁLIDA!. Escolha novamente ou precione 4 para sair '))
else:
    if jogador ==4:
        print ('\n Obrigado por participar do Jogo.')        
print ('\nJO')
sleep (1)
print ('KEN')
sleep (1)
print ('PO!!!')
sleep (1)
print ('\nRobô jogou {}'.format(acoes_do_jogo[bot]))
print ('Você jogou {}'.format(acoes_do_jogo[jogador]))

#add regras do jogo
if bot ==1 and jogador == 2:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==2 and jogador ==1:
    print ('VOCÊ PERDEU!')
elif bot ==3 and jogador ==1:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==1 and jogador == 3:
    print ('VOCÊ PERDEU!')
elif bot ==2 and jogador ==3:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==3 and jogador ==2:
    print ('VOCÊ PERDEU!')
elif bot == jogador:
    print ('EMPATOU!')