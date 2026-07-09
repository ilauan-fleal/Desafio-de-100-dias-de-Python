n_questao = 0

class Perguntas:
    def __init__(self, q_lista):
        self.n_questao = 0
        self.questao_lista = q_lista
    
    #Implementando função , para confirmar se ainda há pergunta disponível!

    def ainda_tem_pergunta(self):
        if self.n_questao < len(self.questao_lista):
            return True
        else:
            return False
    
    #Implementando função, para determinar qual a próxima questão!


    def proxima_questao(self):
        questao_atual = self.questao_lista[self.n_questao]
        self.n_questao += 1
        input(f"Q.{self.n_questao}:{questao_atual.texto}(True/False)")        