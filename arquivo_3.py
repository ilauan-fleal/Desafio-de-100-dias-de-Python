#Revisão

#Calculadora de contas em um restaurante hipotético , considerando as gorjetas!


print("Bem-vindo à calculadora de gorjetas em Python!")

conta = float(input("Qual é o total a ser pago, na conta?\n"))

gorjeta = int(input("Defina o percentual dado ao estabelecimento (10, 12 ou 15)\n"))

total_pessoas = int(input("Qual é o total de pessoas que irão dividir essa conta?:\n"))

gorjeta_percentual = gorjeta/100

valor_pago_de_gorjetas =  conta * gorjeta_percentual #Em R$

valor_pago_na_conta = conta + valor_pago_de_gorjetas

valor_pago_por_pessoa = valor_pago_na_conta/total_pessoas

valor_final = round(valor_pago_por_pessoa, 2)

print(f"O valor final pago por cada um é de R$ {valor_final}")

