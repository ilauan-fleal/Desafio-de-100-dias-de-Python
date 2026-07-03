#Criando função para encontrar aposta mais alta


apostas = {}

def encontrar_aposta_mais_alta(dicionario):
    vencedor = " "
    apostador_mais_elevado = 0
    for apostador in dicionario:
        apostador_soma = dicionario[apostador]
        if apostador_soma > apostador_mais_elevado:
            apostador_mais_elevado = apostador_soma
            vencedor = apostador
    print(f" O vencedor é {vencedor} com uma aposta de {apostador_mais_elevado}.\n")




#Implementação de função com loop para encontrar as apostas



def ParaOuContinua():
    continuar_apostas = True
    while(continuar_apostas):


        nome = input("Insira seu nome:\n")
        preco = float(input("Insira seu valor de aposta em R$:\n"))
        apostas[nome] = preco #Inserção de dados no dicionário!
        deve_continuar = input("Há algum outro apostador? Digite 'sim' ou 'não'.\n")
        if deve_continuar.lower() == 'sim':        
            continue  #retorna para o laço
        elif deve_continuar.lower() == 'não':
            continuar_apostas = False
            encontrar_aposta_mais_alta(apostas)  #Chamada de uma função dentro de outra.
            print("Ok, programa finalizado!\n")
            exit(1)
        else:
            print("Programa encerrado, pois um dado inválido foi inserido!\n")
            exit(1)



#Chamada da função


ParaOuContinua()