import os
import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import numpy

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "verca.mala.mala"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "I6dtS3.E5SG035=="

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

# Tabulka dreviny v naší databázi obsahuje informace o těžbě dřeva podle druhů dřevin a typu těžby. Objem těžby se nachází ve sloupci hodnota.
#Pomocí SQL dotazu do databáze si připrav dvě pandas tabulky:

# tabulka smrk bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska"
smrk=pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt= 'Smrk, jedle, douglaska'", con=engine)
# print(smrk.head())
# smrk.to_csv("smrk.csv")

# tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"
nahodila_tezba=pandas.read_sql("SELECT * FROM dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
# print(nahodila_tezba)
# nahodila_tezba.to_csv("nahodila_tezba.csv")


# Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.
smrk=smrk.sort_values(by="rok")
smrk.plot(kind="bar", y="hodnota", x = "rok", )
# plt.show()

# Vytvoř graf, který ukáže vývoj objemu těžby pro různé typy nahodilé těžby
# Agreguj tabulku nahodila_tezba podle sloupce prictez_txt a na výsledek operace groupby zavolej metodu plot s parametrem legend=True.


# druhy_tezby=nahodila_tezba["prictez_txt"].unique()
# print(druhy_tezby)

vyvoj_tezby_pivot=pandas.pivot_table(nahodila_tezba, index="rok", columns="prictez_txt", values="hodnota", aggfunc=numpy.sum)
vyvoj_tezby_pivot.plot()
plt.show()

# Dobrovolný doplněk
# Porovnej oba grafy:

# Čím je způsobený prudký nárůst těžby jehličnatých stromů cca od roku 2015, který je viditelný v grafu z bodu (2.)?

# Z grafu je patrné, že se jedná o hmyzovou říčinu. Na internetu lze velmi snadno dohledat, že právě v roce 2015 přišla druhá kůrovnovcová
# vlna na Severní Moravu, kde kůrovec napadal hlavně suchem oslabené smrky.

# Kolem roku 2007 vidíme v obou grafech krátkodobý nárůst těžby. Čím byl způsobený (můžeš zkusit dohledat konkrétní událost)?
# Jednalo se o živelnou pohromu - Orkán Kyrill.