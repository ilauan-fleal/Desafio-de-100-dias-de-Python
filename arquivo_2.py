#Criando função para inverter valores de variáveis
glass1 = "milk"
glass2 = "juice"

def InverteValor():
    global glass1  #Referência a um parâmetro global
    global glass2  #Outra referência feita a um parâmetro global
    temp = glass1
    glass1 = glass2
    glass2 = temp
    

#Chamada da função
#As variáveis terão valores trocados, após a chamada da função!
InverteValor()
print(glass1)
print(glass2)