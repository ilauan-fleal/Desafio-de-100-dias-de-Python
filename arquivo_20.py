#Simulador de máquina de café em Python!
lucro = 0


#Primeiro, cria-se um dicionário, contendo todos os itens da máquina!

Itens_maquina = {
    "expresso":{
        "ingredientes":{
            "água":50,
            "café":18,
        },
        "custo":1.5,
    },
    "cafe com leite":{
        "ingredientes":{
            "água":200,
            "leite":150,
            "café": 24,
        },
        "custo":2.5,

    },
    "capuccino":{
        "ingredientes":{
            "água":250,
            "leite": 100,
            "café":24,
        },
        "custo": 3.0,
    }

}


#Depois, tem-se a criação de um dicionário com os recursos que deverão ser utilizados!

recursos = {
    "água":400,
    "leite":200,
    "café":100,
}

#Implementando função, para verificar se tem recursos suficientes!

def tem_recurso_suficiente(Itens_maquina, recursos):
    for x in Itens_maquina:
        if Itens_maquina[x] >= recursos[x]:
            print(f"Desculpe, não há {x} suficiente.\n")
            return False
    return True



#Implementando função, para processar as moedas!


def Processar_Moedas():
    print("Por favor, insira as moedas:\n")
    valor_total = int(input("Quantas moedas  de R$0.01 você tem?\n")) * 0.01
    valor_total += int(input("Quantas moedas de R$0.05 você tem?\n")) * 0.05
    valor_total += int(input("Quantas moedas de R$0.10 você tem?\n")) * 0.10
    valor_total += int(input("Quantas moedas de R$0.25 você tem?\n")) * 0.25
    return valor_total

#Implementando função, para verificar se a transação foi bem-sucedida:


def transacao_bem_sucedida(valor_recebido, custo_da_bebida):
    if valor_recebido >= custo_da_bebida:
        troco = float(round(valor_recebido - custo_da_bebida, 2)) #Determina o troco a ser recebido!
        print(f"Aqui, está seu troco: R${troco}\n")
        global lucro      #Referenciando variável global!
        lucro = lucro + custo_da_bebida
        print(f"Dinheiro na máquina: {lucro}.\n")
        return True
    else:
        print("Desculpe, não há dinheiro suficiente.\n")
        return False
        





#Criando função, para preparar café

def Preparar_Cafe(nome_da_bebida, ingredientes_pedidos, recursos):

    for y in ingredientes_pedidos:
        #Deverão ser descontados dos recursos os ingredientes da bebida solicitada!
        recursos[y] = recursos[y] - ingredientes_pedidos[y]
    print(f"Aqui está sua bebida: {nome_da_bebida}.\n")





def InicializaMaquina(Itens_maquina, recursos):
    
    while 1:
        
        print("Expresso/café-com-leite/capuccino:\n")
        print("1) expresso.\n")
        print("2) cafe com leite.\n")
        print("3) capuccino.\n")
        print("4) relatorio.\n")
        print("5) off para sair.\n")
        escolha = input("Qual tipo de bebida desejas?\n").lower()
        if escolha == "off".lower():
            break
        elif escolha == "relatorio".lower():
            print(f"Água: {recursos["água"]}.\n")
            print(f"Leite:{recursos["leite"]}.\n")
            print(f"Café: {recursos["café"]}.\n")
      
        elif escolha == "expresso" or escolha == "cafe com leite" or escolha == "capuccino":
            bebida = Itens_maquina[escolha] #Um item contido no dicionário, será escolhido!    
            if tem_recurso_suficiente(bebida["ingredientes"], recursos):
                print("Ok...")
                pagamento = Processar_Moedas()
                if transacao_bem_sucedida(pagamento, bebida["custo"]):
                    Preparar_Cafe(escolha, bebida["ingredientes"], recursos)
                    print("Deseja fazer outro pedido ou o sistema pode ser encerrado?\n")
                    print("1 -> Fazer outra transação.\n")
                    print("2 -> Encerrar o programa.\n")
                    nova_escolha = int(input())
                    if nova_escolha == 1:
                        continue
                    elif nova_escolha == 2:
                        print("Ok, programa encerrado.\n")
                    else:
                        print("Dado inválido, programa, encerrado.\n")
                        exit(1)
        else:
            print("Deixe-me ver, dado inválido, o sistema será executado novamente.\n")
            continue

#Chamando função de inicialização da máquina , cujos parâmetros são dois dicionários diferentes!

InicializaMaquina(Itens_maquina, recursos)