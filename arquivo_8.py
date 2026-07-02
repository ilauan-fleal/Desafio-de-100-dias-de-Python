

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S','T','U', 'V' 'W', 'X', 'Y', 'Z', 'a','b', 'c', 'd', 'e','f', 'g','h','i','j',
            'k', 'l', 'm', 'n','o','p','q', 'r','s','t','u','v','w','x','y', 'z']

texto = input("Insira sua mensagem:\n").lower()

numero = int(input("Insira o valor, no qual irá deslocá-lo:\n"))

#Unindo função de criptografar e descriptografar em um único programa!!

escolha = input("Escreva 'descriptografar', para decifrar uma mensagem, ou então 'criptografar' para protegê-la:\n")


def Criptografa_e_Descriptografa(texto_original, bit_deslocado, criptografa_ou_descriptografa):
    texto_cifra = " "
    for letra in texto_original:
        if letra not in alfabeto:
            texto_cifra = texto_cifra + letra
        if criptografa_ou_descriptografa == "descriptografar".lower():
            posicao_bit = alfabeto.index(letra) - bit_deslocado #ATENÇÃO!
            posicao_bit = posicao_bit % len(alfabeto)
            texto_cifra = texto_cifra + alfabeto[posicao_bit]
        
            
        elif criptografa_ou_descriptografa == "criptografar".lower():
    
            posicao_bit = alfabeto.index(letra) + bit_deslocado #ATENÇÃO!
            posicao_bit = posicao_bit % len(alfabeto)
            texto_cifra = texto_cifra + alfabeto[posicao_bit]
    
        else:
            print("Dado inserido inválido, execute o programa novamente!!\n")
        
    print(f"Resultado encontrado: {texto_cifra}\n")
          


Criptografa_e_Descriptografa(texto, numero, escolha) #Chamada da função!


#Implementar loop while, denntro de uma função, para decidir continuidade do programa!


def ParaOuContinua():
    continuar = True
    while continuar:
        print("Deseja criptografar e/ou descriptografar algo mais?\n")
        print("1  -> Continua.\n")
        print("0. -> Encerra.\n")
        res = input()
        if res != 1 and res != 0:

            print("O dado inserido, não corresponde às inserções acima, digite-o novamente.\n")
            continue
        elif res == 1:

            texto = input("Insira sua mensagem:\n").lower()
            numero = int(input("Insira o valor, no qual irá deslocá-lo:\n"))
            escolha = input("Escreva 'descriptografar', para decifrar uma mensagem, ou então 'criptografar' para protegê-la:\n")
            Criptografa_e_Descriptografa(texto, numero, escolha)
        else:
            print("Ok, programa encerrado, conforme solicitado.\n")
            exit(1)

#Chamada da função para decidir se o usuário para ou continua!

ParaOuContinua()