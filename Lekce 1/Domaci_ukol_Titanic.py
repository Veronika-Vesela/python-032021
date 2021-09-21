import requests
import pandas
import numpy

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/7cdd66d0313f60fe177fbdbd7f3b87b079cacd67/01_pandas/01/ukol/tested.csv?token=AVVCVO7DXW7537OVKWELJM3BJGRMA")
#open("tested.csv", 'wb').write(r.content)

cestujici=pandas.read_csv("tested.csv")


#V souboru tested.csv najdeš informace o cestujících na zaoceánském parníku Titanic. Vytvoř kontingenční tabulku, která
#porovná závislost mezi pohlavím cestujícího (soupec Sex), třídou (sloupec Pclass), ve které cestoval, a tím, jesti
#přežil potopení Titanicu (sloupec Survived). Pro data můžeš použít agregaci numpy.sum, která ti spočte absolutní počet
#přeživších pro danou kombinaci, nebo numpy.mean, která udá relativní počet přeživších pro danou kombinaci.

pivot_prezivsi=pandas.pivot_table(cestujici, index="Pclass", columns="Sex", values="Survived", aggfunc=numpy.sum, margins=True, margins_name="Celkem přeživších")
print(pivot_prezivsi)

pivot_utonuli=pandas.pivot_table(cestujici, index="Pclass", columns="Sex", values="Survived", aggfunc="count", margins=True, margins_name="Celkem cestujících")
print(pivot_utonuli)

pivot_prumer=pandas.pivot_table(cestujici, index="Pclass", columns="Sex", values="Survived", aggfunc=numpy.mean)
print(pivot_prumer)



