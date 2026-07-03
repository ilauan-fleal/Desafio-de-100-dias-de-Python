#Projeto de calculadora no Desafio Python de 100 dias!

x = int(input("Introduza um valor para x:\n"))
y = int(input("Introduza um valor para y:\n"))

#Implementando funções da calculadora!

def Soma(x,y):
    return x + y

def Subtrai(x,y):
    return x - y

def Multiplica(x,y):
    return x * y

def Divide(x,y):
    return x / y


#As funções serão agregadas dentro de um dicionário, cujas chaves, são as quatro operações aritméticas básicas!

dicionario = {'+': Soma, '-':Subtrai, '*': Multiplica, '/': Divide}


#Escrevendo função para selecionar operação!

 

def SelecionarOperacao(x,y):
    
    print("Escolha uma operação aritmética para realizar com esses números...\n")
    listaOperacoes = ['+', '-', '/', '*']
    for n in listaOperacoes:
        print(n)
    escolha = input("Digite o símbolo à operação correspondente:\n")
    if escolha in dicionario.keys():
        print("Ok, processando...\n")
        #Esse laço for irá percorrer todas as chaves do dicionário!
    
        if escolha == '+':

            print("Será realizada a adição entre os números:\n")
            print(dicionario['+'](x,y))
            
        elif escolha == '-':
            print("Será realizada a subtração entre os números:\n")
            print(dicionario['-'](x,y))
            
        elif escolha == '*':
            print("Será realizada a multiplicação entre os números:\n")
            print(dicionario['*'](x,y))
                
        elif escolha == '/':
            print("Será realizada a divisão entre os números:\n")
            print(dicionario['/'](x,y))
            
    elif escolha not in dicionario.keys():
        print("Valor inválido, digitado, execute o programa novamente!\n")
        exit(1)
    continuar = 1
    #Looping, para possibilitar continuidade de usufruto do programa, ou seja realizar novos cálculos, se o usuário assim desejar
    while(continuar):
        print("Deseja fazer outra operação ou encerrar o programa!\n")
        print('1 -> Continua a realizar operações:\n')
        print('2 -> O programa é encerrado.\n')
        novaEscolha = int(input())
        if novaEscolha == 1:
            x = int(input("Introduza um valor para x:\n"))
            y = int(input("Introduza um valor para y:\n"))
            SelecionarOperacao(x,y)
        elif novaEscolha == 2:
            print("Ok, programa encerrado, conforme desejado.\n")
            exit(1)
        else:
            print("Dado inválido, digite-o novamente:\n")
            novaEscolha = int(input())
#Chamada da função!


SelecionarOperacao(x,y)