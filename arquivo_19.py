#Importando dados de um dicionário do arquivo anterior!
import random
from arquivo_18 import dados


#Criando função para estruturar dado!


def Estruturar_Dado(conta):
    nome_da_conta = conta["nome"] #Armazena valor da chave 'nome'
    descricao_da_conta = conta["descricao"] #Armazena valor da chave 'descricao'
    pais_da_conta = conta["pais"] #Armazena valor da chave 'pais'
    return f"{nome_da_conta} a {descricao_da_conta} from .{pais_da_conta}"





#Implementar função, para verificar a respostas!

def VerificarResposta(palpite_inserido, conta_a_seguidores, conta_b_seguidores):
    if conta_a_seguidores > conta_b_seguidores and palpite_inserido == "A".lower():
        if conta_a_seguidores > conta_b_seguidores:
            if palpite_inserido == "A".lower():
                return True
            else:
                return False
    elif conta_b_seguidores > conta_a_seguidores and palpite_inserido == "B".lower():
        if conta_b_seguidores > conta_a_seguidores:
            if palpite_inserido == "B".lower():
                return True
            else:
                return False
   
        





#Implementando looping , para verificar se o jogo deveria continuar:
def IniciaJogoComparativo():
    recorde = 0
    jogo_deveria_continuar = True
    while jogo_deveria_continuar:
        conta_a = random.choice(dados)
        conta_b = random.choice(dados)
        if conta_a == conta_b:
            conta_b = random.choice(dados)
        print(f"Compare A: {Estruturar_Dado(conta_a)}.\n")
        print(f"Contra B: {Estruturar_Dado(conta_b)}.\n")
        palpite = input("Quem tem mais seguidores ? Digite 'A' ou 'B'?\n").lower()
        if palpite != 'A'.lower() and palpite != 'B'.lower():
            print("Dado inserido, incorretamente.\n")
            print("Execute o programa novamente!\n")
            exit(1)
        conta_a_seguidores = conta_a["seguidores"]
        conta_b_seguidores = conta_b["seguidores"]
        esta_correto = VerificarResposta(palpite, conta_a_seguidores, conta_b_seguidores)
        if esta_correto:
                
                recorde = recorde + 1
                print(f'Você está correto! Seu atual recorde é {recorde}.\n')
        else:
                print(f'Desculpe, isso está errado. O recorde final é: {recorde}.\n')
                jogo_deveria_continuar = False



#Chamada da função!


IniciaJogoComparativo()