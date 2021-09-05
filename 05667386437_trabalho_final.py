import pandas as pd
import matplotlib.pyplot as plt

# dados tarifarios da ANEEL
dados = pd.read_csv("https://raw.githubusercontent.com/gustavopompeu/ENAP/master/TarifaFornecimentoResidencial.csv",
encoding = "iso8859_16")

# descricao generica
print(dados.head())

# medida resumo (media)
print(dados["VlrTUSDConvencional"].mean())
# medias separadas para cada tipo de concessao
print(dados.groupby("nomConcessao")["VlrTUSDConvencional"].mean())
# medias separadas para cada regiao
print(dados.groupby("SigRegiao")["VlrTUSDConvencional"].mean())
# medias separadas para cada tipo de concessao e regiao
print(dados.groupby(["nomConcessao","SigRegiao"])["VlrTUSDConvencional"].mean())

# medida resumo (mediana)
print(dados["VlrTUSDConvencional"].median())
# medias separadas para cada tipo de concessao
print(dados.groupby("nomConcessao")["VlrTUSDConvencional"].median())
# medias separadas para cada regiao
print(dados.groupby("SigRegiao")["VlrTUSDConvencional"].median())
# medias separadas para cada tipo de concessao e regiao
print(dados.groupby(["nomConcessao","SigRegiao"])["VlrTUSDConvencional"].median())

# geral
print(dados["VlrTUSDConvencional"].describe())

# quantis e percentis

# exemplo 1: percentil 10%
print(dados["VlrTUSDConvencional"].quantile(.1))
# exemplo 2: 1o quartil (25%)
print(dados["VlrTUSDConvencional"].quantile(.25))

fig, ax = plt.subplots()
dados["SigRegiao"].value_counts().plot.bar(color=["blue", "#ff4000", "yellow", "silver", "gold"])
ax.set_ylabel("Contagem")
ax.set_xlabel("Região")
ax.set_ylim(0,100)
plt.show()

dados["SigRegiao"].value_counts().plot.pie()
ax.set_ylabel("Contagem")
ax.set_xlabel("Região")
plt.show()

#########################

import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns


viagens = pd.read_csv("https://dados.antt.gov.br/dataset/1372ecf0-22a5-49cc-8244-5bcda32e658b/resource/b82d9945-899c-44ec-a149-bea94d4e79d1/download/licenca_viagem_internacional_2019.csv",
delimiter=";", encoding="latin1")
viagens.head()

pd.crosstab(viagens.uf_municipio_origem,viagens.pais_destino)



def determina_regiao(uf):
if uf in ("DF" , "MS" , "MT" , "GO"):
return "CO"
if uf in ( "AC" , "RO" , "PA"):
return "N"
if uf in ("BA" , "MA" , "PB" , "PI" , "RN"):
return "NE"
if uf in ( "RS" , "PR" , "SC"):
return "S"
if uf in ( "SP" , "ES" , "MG" , "RJ"):
return "SE"

viagens["regiao"] = viagens.uf_municipio_origem.map(determina_regiao)


viagens.head()



pd.crosstab(viagens.regiao, viagens.pais_destino)



minha_frequencia = pd.crosstab(viagens.total_passageiros,viagens.pais_destino)
minha_frequencia


#pd.cut(v 