import pandas as pd
import re

dados_portugues =  pd.read_csv("base_dados/stackoverflow_portugues.csv")
dados_ingles = pd.read_csv("base_dados/stackoverflow_ingles.csv")
dados_espanhol = pd.read_csv("base_dados/stackoverflow_espanhol.csv")

questao_portugues = dados_portugues.Questão[5]
# print(questao_portugues)

# Retorna uma lista com todas as tags html no texto
# retorno = re.findall(r"<.*?>", questao_portugues)
# print(retorno)


retorno_sub = re.sub(r"<.*?>", "  T-----E------S------T----E  ", questao_portugues)
print(retorno_sub)

