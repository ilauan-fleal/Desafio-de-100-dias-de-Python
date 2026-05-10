#desafio -> pedra, papel e tesoura(jogo)
import random
pedra = '''
     ---------------
----              ---- )
                 (---- )
                 (---- )
                 (---- )
-----            (---- )
     ---------------


'''


papel = '''

   ----------
---      -------)----
             _ _ _ _ _ _)
             _ _ _ _ _ _)
             _ _ _ _ _ _)
---          _ _ _ _ _)
    _ _ _ _ _ _ _ _)


'''


tesoura = '''
   -----------
---       ----)------
              _ _ _ _)
          _ _ _ _ _ _)
        (_ _ _ _ _)   
---     (_ _ _)
    _ _




'''

lista = [pedra, papel, tesoura]











def InicializaJogo(lista):
    print("Olá, bem-vindo ao jogo clássico, de pedra , papel e tesoura:\n")
    print("Escolha:\n")
    print("0  -> pedra.\n")
    print("1. -> papel.\n")
    print("2. -> tesoura.\n")
    escolhaPessoa = int(input())
    
   
    if(escolhaPessoa == 0):
        x = random.randint(0,len(lista)-1)
        print("Você escolheu:\n")
        print(lista[0])
        print("E a máquina escolheu:\n")
        print(lista[x])
        Ganhou(escolhaPessoa,x)
        
    elif(escolhaPessoa == 1):
        x = random.randint(0,len(lista)-1)
        print("Você escolheu:\n")
        print(lista[1])
        print("E a máquina escolheu:\n")
        print(lista[x])
        Ganhou(escolhaPessoa,x)
        
    elif(escolhaPessoa == 2):
        x = random.randint(0,len(lista)-1)
        print("Você escolheu:\n")
        print(lista[2])
        print("E a máquina escolheu:\n")
        print(lista[x])
        Ganhou(escolhaPessoa,x)
        
    else:
        print("Escolha inválida, o programa será compilado novamente!\n")
        InicializaJogo(lista)

#Criando função , para definir, o jogador vitorioso.

def Ganhou(jogador,x):
    if(jogador == x):
        print("Empate!")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            
    elif(jogador == 0 and x == 1):
        print("A IA venceu , pois escolheu papel contra pedra.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    elif(jogador == 1 and x == 0):
        print("O jogador venceu , pois escolheu papel contra pedra.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    elif(jogador == 2 and x == 1):
        print("O jogador venceu , pois escolheu tesoura contra papel.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    elif(jogador == 1 and x == 2):
        print("A IA venceu , pois escolheu tesoura contra papel.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    elif(jogador == 2 and x == 0):
        print("A IA venceu pois escolheu pedra contra tesoura.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    elif(jogador == 0 and x == 2):
        print("O jogador venceu pois escolheu pedra contra tesoura.\n")
        print("Para jogar novamente tecle 1, ou 0 para sair!\n") 
        escolha = int(input())
        if(escolha == 1):
            InicializaJogo(lista)
        elif(escolha == 0):
            print("Ok, programa encerrado!\n")
            exit(1)
        else:
            print("Dado inválido, programa encerrado!")
            exit(1)
    

#Chamando a função

InicializaJogo(lista)