#Implementando função de criptografia em Python

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S','T','U', 'V' 'W', 'X', 'Y', 'Z', 'a','b', 'c', 'd', 'e','f', 'g','h','i','j',
            'k', 'l', 'm', 'n','o','p','q', 'r','s','t','u','v','w','x','y', 'z']

texto = input("Insira sua mensagem:\n").lower()

numero = int(input("Insira o valor, no qual irá deslocá-lo:\n"))

def Criptografar(texto_original, bit_deslocado):
    texto_cifra = " "
    for letra in texto_original:
        posicao_bit = alfabeto.index(letra) + bit_deslocado
        posicao_bit = posicao_bit % len(alfabeto)
        texto_cifra = texto_cifra + alfabeto[posicao_bit]
    print(f"Aqui o resultado da codificação : {texto_cifra}\n")

#Chamada da função de criptografia!


Criptografar(texto, numero)

#Implementando função de descriptografar:

def Descriptografar(texto_original, bit_deslocado):
    texto_cifra = " "
    for letra in texto_original:
        posicao_bit = alfabeto.index(letra) + bit_deslocado
        posicao_bit = posicao_bit % len(alfabeto)
        texto_cifra = texto_cifra + alfabeto[posicao_bit]
    print(f"Aqui o resultado da decodificação: {texto_cifra}\n")

#Chamada da função de descriptografia!

Descriptografar(texto, numero)