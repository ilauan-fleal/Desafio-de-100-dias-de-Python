#Implementando função em Python, para verificar número primo!

y = int(input("Digite um número primo:\n"))


def VerificaValor(x):
    if(x == 1):
        return True
    elif(x == 2):
        return True
    elif(x == 3):
        return True
    elif(x == 4):
        return False
    else:
        
        primo = True
        for z in range(3, x, 2):
          
          
        
            if(x % z == 0):
                primo = False
                break


        if primo:
            return True
        else:
            return False


resultado  = VerificaValor(y)

print(f"{resultado}")