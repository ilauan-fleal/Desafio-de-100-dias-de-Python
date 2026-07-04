#Criando jogo de adivinhação
import random

#Definindo algumas variáveis globais!!

NIVEL_FACIL = 10
NIVEL_DIFICIL = 5

#Implementando função para determinar dificuldade do jogo!

def DefinirDificuldade():
    nivel = input("Selecione a dificuldade do jogo: Digite 'simples' para mais tentativas ou 'complexo' para menos tentativas.\n")
    if nivel == "simples".lower():
        return NIVEL_FACIL - 1
    elif nivel == "complexo".lower():
        return NIVEL_DIFICIL - 1
    else:
        print("Dado inválido, execute, o programa novamente.\n")
        exit(1)
    

#Criando função, para verificar a resposta:


def VerificaResposta(palpite_usuario, resposta_atual,vez):
    if palpite_usuario > resposta_atual:
        print("Palpite muito elevado.\n")
        return vez - 1
    elif palpite_usuario < resposta_atual:
        print("Palpite muito baixo.\n")
        return vez - 1
    else:
        print(f"Você acertou, a resposta é {resposta_atual}.\n")
        exit(1)



#Criando função , para inicializar o jogo!


def Jogo():
    print("Bem-vindo ao jogo de adivinhação em Python!\n")
    print("Penso em um valor que vai de 1 até 100.\n")
    res = random.randint(1,100)
    vez = DefinirDificuldade() #A variável vez, será igual ao retorno da função DefinirDificuldade()
    print(f"Você tem {vez} tentativas restantes, para adivinhar o número.\n")
    palpite = 0
    while palpite != res:
        palpite = int(input("Dê um palpite:\n"))
        vez = VerificaResposta(palpite, res, vez)
        if vez == 0:
            print("Você está sem tentativas.\n")
            exit(1)
        elif palpite != res:
            print("Jogue de novo.\n")


#Chamada da função!

Jogo()