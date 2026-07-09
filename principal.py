
from dados import dados_estruturados
from modeloQuestionario import Questionario
from ProcessaPerguntas import Perguntas
banco_de_questoes = []

for x in dados_estruturados:
    q_texto = x["text"]
    q_resposta = x["answer"]
    outra_questao = Questionario(q_texto,q_resposta)
    banco_de_questoes.append(outra_questao)


pergunta = Perguntas(banco_de_questoes)
pergunta.proxima_questao()


def Exibir():
    while pergunta.ainda_tem_pergunta():
        pergunta.proxima_questao()

#Chamada da função!

Exibir()