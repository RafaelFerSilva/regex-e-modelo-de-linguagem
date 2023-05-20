import pandas as pd
dados_portugues =  pd.read_csv("base_dados/stackoverflow_portugues.csv")
dados_ingles = pd.read_csv("base_dados/stackoverflow_ingles.csv")
dados_espanhol = pd.read_csv("base_dados/stackoverflow_espanhol.csv")
print(dados_espanhol.Questão[0])
