#Implementando simulação de jogo de cartas em Python(BlackJack)

lista_cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#Listas , nas quais os dados serão agregados!

cartas_usuario = []

cartas_computador = []




import random

#Criando função para distribuir cartas no jogo.


def Distribui_Cartas(lista_cartas):
    #será selecionada uma carta aleatória!!
    carta_selecionada = random.choice(lista_cartas)
    return carta_selecionada


#Criando outra função para agregar cartas aos usuários e ao computador!


def Gerar_Cartas():
    for a in range(2):
        cartas_usuario.append(Distribui_Cartas(lista_cartas))
        cartas_computador.append(Distribui_Cartas(lista_cartas))



#Criar função para calcular o recorde!



def Calcular_Recorde(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    elif 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

#Continuando implementação!


#Criar função de comparação!

def Compara(recorde_de_usuario, recorde_de_computador):
    if recorde_de_usuario == recorde_de_computador:
        print("Deu empate.")
    elif recorde_de_computador == 0:
        print("Perdeu, o oponente tem um BlackJack.")
    elif recorde_de_usuario == 0:
        print("Vence com o BlackJack.")
    elif recorde_de_usuario > 21:
        print("Você perdeu.")
    elif recorde_de_computador > 21:
        print("O oponente perdeu, você venceu.")
    elif recorde_de_usuario > recorde_de_computador:
        print("Você vence.")
    else:
        print("Você perdeu.")


#Criando função para verificar o jogo

def VerificaJogo():

    #Chamada de função, para gerar cartas!


    Gerar_Cartas()
    jogo_finalizado = False
    while not jogo_finalizado:

        recorde_de_usuario = Calcular_Recorde(cartas_usuario)
        recorde_de_computador = Calcular_Recorde(cartas_computador)
        print(f"Suas cartas: {cartas_usuario} , seu recorde é {recorde_de_usuario}.\n")
        print(f"Primeira carta do computador: {cartas_computador[0]}.\n")
        Compara(recorde_de_usuario, recorde_de_computador)
#Verificação de recorde!


        if recorde_de_usuario == 0 or recorde_de_computador == 0 or recorde_de_usuario > 21:
            jogo_finalizado = True
        else:

            escolha_usuario = int(input("Digite 1 para obter uma nova carta, ou então 0 para passar adiante.\n"))
            if escolha_usuario == 1:
                cartas_usuario.append(Distribui_Cartas(lista_cartas))
            elif escolha_usuario == 0:
                jogo_finalizado = True
            else:

                print("Comando inválido, tente novamente.\n")
                continue #Retorno ao looping!




    while recorde_de_computador != 0 and recorde_de_computador < 17:
        cartas_computador.append(Distribui_Cartas(lista_cartas))
        recorde_de_computador = Calcular_Recorde(cartas_computador)



#Chamada da função!


VerificaJogo()