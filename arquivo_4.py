#desafio -> lista + número randômico
import random
MyList = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#Arquivo 4
def ImprimeValorAleatorio():

    print(MyList[(random.randint(0,len(MyList)))])

#Chamada da função

ImprimeValorAleatorio()

