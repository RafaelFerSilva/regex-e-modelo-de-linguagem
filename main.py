import pandas as pd
import re
from timeit import timeit

dados_portugues =  pd.read_csv("base_dados/stackoverflow_portugues.csv")
dados_ingles = pd.read_csv("base_dados/stackoverflow_ingles.csv")
dados_espanhol = pd.read_csv("base_dados/stackoverflow_espanhol.csv")

questao_portugues = dados_portugues.Questão[5]
# print(questao_portugues)

# Retorna uma lista com todas as tags html no texto
# retorno = re.findall(r"<.*?>", questao_portugues)
# print(retorno)

# Substituir um texto por outro
# retorno_sub = re.sub(r"<.*?>", "  T-----E------S------T----E  ", questao_portugues)
# print(retorno_sub)


# Transformar uma string em um regex e retornar onde o caracter está
# retorno_search = re.search(r"70", "89745615749846541987945615749841568945679854170")
# print(retorno_search)

# Transformar uma string em um regex e retornar onde o caracter está -  Mais rápido
# regex = re.compile(r"70")
# retorno_compile = regex.search("89745615749846541987945615749841568945679854170")
# print(retorno_compile)

# Comparando os métodos
setup = """import re"""
tempo = timeit("""re.search(r"70", "89745615749846541987945615749841568945679854170")""", setup)
print(tempo)

setup = """import re 
regex = re.compile(r"70")"""
tempo = timeit("""regex.search("89745615749846541987945615749841568945679854170")""", setup)
print(tempo)

