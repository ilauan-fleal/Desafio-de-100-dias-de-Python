import random 


def Mutacao(lista):
    nova_lista = []
    novo_item = 0
    for x in lista:
        novo_item = novo_item + x * 2
        novo_item = novo_item + random.randint(1,3)   
        nova_lista.append(novo_item)
    print(nova_lista)

Mutacao([1,2,3,4,5,6,7,8,9])