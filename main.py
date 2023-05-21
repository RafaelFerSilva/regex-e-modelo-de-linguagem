import pandas as pd
import re
from timeit import timeit

dados_portugues = pd.read_csv("base_dados/stackoverflow_portugues.csv")
dados_ingles = pd.read_csv("base_dados/stackoverflow_ingles.csv")
dados_espanhol = pd.read_csv("base_dados/stackoverflow_espanhol.csv")

questao_portugues = dados_portugues.Questão[5]
questao_espanhol = dados_espanhol.Questão[5]
questao_ingles = dados_ingles.Questão[5]

regex_html = re.compile(r"<.*?>")
regex_code = re.compile(r"<code>(.|(\n))*?</code>")

def remover(textos, regex):
    if type(textos) == str:
        return regex.sub("", textos)
    else:
        return [regex.sub("", texto) for texto in textos]


def substituir_codigo(textos, regex):
    if type(textos) == str:
        return regex.sub("CODE", textos)
    else:
        return [regex.sub("CODE", texto) for texto in textos]


questoes_port_sem_codigo = substituir_codigo(dados_portugues.Questão, regex_code)
questoes_port_sem_codigo_sem_tag = remover(questoes_port_sem_codigo, regex_html)

questoes_esp_sem_codigo = substituir_codigo(dados_espanhol.Questão, regex_code)
questoes_esp_sem_codigo_sem_tag = remover(questoes_esp_sem_codigo, regex_html)

questoes_ing_sem_codigo = substituir_codigo(dados_ingles.Questão, regex_code)
questoes_ing_sem_codigo_sem_tag = remover(questoes_ing_sem_codigo, regex_html)

dados_portugues["sem_code_sem_tag"] = questoes_port_sem_codigo_sem_tag
dados_espanhol["sem_code_sem_tag"] = questoes_esp_sem_codigo_sem_tag
dados_ingles["sem_code_sem_tag"] = questoes_ing_sem_codigo_sem_tag


print(dados_espanhol.sem_code_sem_tag[0])



