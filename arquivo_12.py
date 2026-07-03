#Escrevendo função para determinar se um ano é bissexto!

#REGRA:

#Um ano bissexto, é aquele, no qual possui um dia a mais contado no calendário!

#Para determinar se um determinado é bissexto ou não , deve-se seguir os seguintes passos:

#Verificar se ele é múltiplo de 4

#Se múltiplo de 100, obrigatoriamente, deverá ser múltiplo de 400, do contrário não é bissexto.




def VerificaAnoBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:        
        return True
    else:
        return False
    
x = VerificaAnoBissexto(2026)
print(x)


