#Elaborando um simples jogo de forca em Python!
import random

ListaPalavra = ["abacate", "laranja", "morango"]

LetrasCorretas = []

PalavraEscolhida = random.choice(ListaPalavra)



estagios = ["""

 +----+
 |    +
 |    +
 O    +
      +
      +
=======
"""
,

"""
            
 +----+
 |    +       
 |    +
 O    +
 |    +
      +
=======

"""

,

"""


  +-----+
  |     +
  |     +
  o     +
--|    +
       +
========

"""
,

"""


  +-----+
  |     +
  |     +
  o     +
--|--   +
        +
========

"""

,



"""


  +-----+
  |     +
  |     +
  o     +
--|--   +
   |    +
========

"""
,



"""


  +-----+
  |     +
  |     +
  o     +
--|--   +
 | |    +
========

"""





]





exibir = " "

#Função geradora da palavra

def GerarPalavra(ListaPalavra):
    PalavraEscolhida = random.choice(ListaPalavra)
    local = "_"        

    ComprimentoPalavra = len(PalavraEscolhida)

    for posicao in range(ComprimentoPalavra):
        local = local + "_"


    print(local)


GerarPalavra(ListaPalavra)

#Função para verificar o palpite dado pelo jogador
    
def VerificaPalpite(PalavraEscolhida,exibir,LetrasCorretas):
    palpite = input("Forneça um palpite:")
    tentativas = -1
    for letra in PalavraEscolhida:
        if letra == palpite:
            exibir = exibir + letra
            LetrasCorretas.append(palpite) 
            #Agregando letra inserida no palpite no final da lista criada!
        elif letra in LetrasCorretas: #Se a letra estiver contida na lista LetrasCorretas
            exibir = exibir + letra    
        
            
            

        else:

            exibir = exibir + "_"
            
        
    print(exibir)
    #O laço só será executado se o palpite fornecido não estiver presente na palavra escolhida.
    if palpite not in PalavraEscolhida:
        tentativas = tentativas + 1 #incremento
        print(estagios[tentativas])
        if tentativas > 6:
            print("Você perdeu.\n")
            exit(1) #Programa encerrado

    
#Função para verificar se o jogador acertou


def Acertou(PalavraEscolhida):
    ComprimentoPalavra = len(PalavraEscolhida)
    comprimentoHipotetico = 1
    
    while True:
    
        VerificaPalpite(PalavraEscolhida,exibir,LetrasCorretas)
        comprimentoHipotetico = comprimentoHipotetico + 1
        if(comprimentoHipotetico == ComprimentoPalavra):
            break
         
    print("Palavra acertada!")



Acertou(PalavraEscolhida) 


