#Nesse arquivo, será exibido um programa em Python com as próprias classes já construídas!!

#Classe usuário

#Com os atributos, inicializados, pelo construtor: cod_identificador, nome, total_seguidores.

class Usuario:
    def __init__(self, cod_identificador, nome):
        self.cod_identificador = cod_identificador
        self.nome = nome
        self.total_seguidores = 0
        self.total_seguindo = 0
        #Definindo método para classe usuário --> método seguir!
    def seguir(self, usuario):
        usuario.total_seguidores += 1
        self.total_seguindo += 1



user_1 = Usuario("001", "Alpha")
user_2 = Usuario("002", "Beta")

#Chamada do objeto junto do método associado!



user_1.seguir(user_2)


print(user_1.total_seguidores)
print(user_2.total_seguidores)
print(user_1.total_seguindo)
print(user_2.total_seguindo)









