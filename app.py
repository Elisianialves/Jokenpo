from random import randint
from time import sleep

def introducao ():
    print ('¨'*80)
    print ('                            VAMOS JOGAR JOKENPO                           ')
    print ('     Pedra ganha de Tesoura, Tesoura ganha de Papel, Papel ganha de Pedra.')
    print ('¨'*80)
    nome = input('\nQual seu nome? ').capitalize()
    sleep (1)
    print ('Bem-Vindo(a) ao Jogo {}'.format(nome))
    sleep (0.8)
introducao()

# jogo
acoes_do_jogo = ('','Pedra', 'Papel', 'Tesoura', 'Sair')
bot = randint (1,3)
print ('\nEscolha sua opção:')
print (' [1] Pedra\n [2] Papel\n [3] Tesoura\n')
print ('OU APERTE 4 PARA SAIR.\n ')
sleep (1)
jogador = int(input('Qual é sua jogada? '))
while jogador not in (1,2,3,4):
     jogador = int (input('JOGADA INVÁLIDA!. Escolha novamente ou pressione 4 para sair '))
else:
    if jogador ==4:
        input ('\nObrigado por participar do Jogo.')  
print ('\nJO')
sleep (1)
print ('KEN')
sleep (1)
print ('PO!!!')
sleep (1)
print ('\nRobô jogou {}'.format(acoes_do_jogo[bot]))
print ('Você jogou {}\n'.format(acoes_do_jogo[jogador]))

# regras do jogo
if bot ==1 and jogador == 2:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==2 and jogador ==1:
    print ('QUE PENA VOCÊ PERDEU. ROBÔ ESTÁ COM SORTE.')
elif bot ==3 and jogador ==1:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==1 and jogador == 3:
    print ('QUE PENA VOCÊ PERDEU. ROBÔ ESTÁ COM SORTE.')
elif bot ==2 and jogador ==3:
    print ('PARABÉNS VOCÊ GANHOU!')
elif bot ==3 and jogador ==2:
    print ('QUE PENA VOCÊ PERDEU. ROBÔ ESTÁ COM SORTE.')
elif bot == jogador:
    print ('EMPATOU!')
